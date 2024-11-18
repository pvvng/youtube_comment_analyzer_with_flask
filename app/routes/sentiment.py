# flask
from flask import request, jsonify, Blueprint
from flask_cors import CORS

# logger
import logging

# json
import json
from json.decoder import JSONDecodeError

# 데이터 처리 함수
from app.utils.my_functions.process_received_data import process_received_data
# 형태소 분석
from konlpy.tag import Okt
# sentiment 모델 불러오기
import onnxruntime as ort
# import numpy as np
from transformers import AutoTokenizer

# api key 검증
from functools import wraps
import os

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 블루프린트 정의
sentiment_bp = Blueprint('sentiment', __name__)

# api key 확인
VALID_API_KEYS = [
    os.getenv("API_KEY_ADMIN", None),
    os.getenv("API_KEY_SUB", None),
]

def require_api_key(f):
    """API Key 검증 데코레이터"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("YOUTUVIEW-API-KEY")  # 요청 헤더에서 API Key 가져오기
        if not api_key or api_key not in VALID_API_KEYS:
            logger.warning(f"Unauthorized request with API Key: {api_key}")
            return jsonify({"error": "Unauthorized. Invalid or missing API Key."}), 401
        return f(*args, **kwargs)
    return decorated_function

# ONNX 모델 및 형태소 분석기 초기화
okt = Okt()
ort_session = ort.InferenceSession("app/models/kcbert_model.onnx")
model_path = "app/models/models-steam-fp16"
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 허용된 Origin 목록
ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:3001", "https://youtuview.netlify.app"]

# CORS 설정: 허용된 Origin만 허용
CORS(sentiment_bp, origins=ALLOWED_ORIGINS)

# 공통 에러 핸들러
@sentiment_bp.app_errorhandler(413)
def request_entity_too_large(e):
    return jsonify({"error": "Payload too large"}), 413

@sentiment_bp.app_errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request", "details": str(e)}), 400

@sentiment_bp.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "details": str(e)}), 500

# API 요청 전 도메인 제한
@sentiment_bp.before_request
def restrict_origin():
    origin = request.headers.get("Origin")
    if origin and origin not in ALLOWED_ORIGINS:
        return jsonify({"error": f"Origin {origin} is not allowed"}), 403
    
# POST 요청을 처리할 API 엔드포인트
@sentiment_bp.route('/analyze', methods=['POST'])
@require_api_key
def receive_data():
    try:
        # 받은 파일 댓글 데이터 변환
        file = request.files['file']
        if not file:
            logger.warning("No file provided in the request")
            return jsonify({"error": "No file provided"}), 400

        # MIME 타입 확인
        if file.mimetype != 'text/plain':
            logger.warning(f"Invalid file type: {file.mimetype}")
            return jsonify({"error": f"Invalid file type: {file.mimetype}. Only 'text/plain' is allowed."}), 400

        if not file.filename.endswith('.txt'):
            logger.warning("Invalid file extension")
            return jsonify({"error": "Invalid file extension. Only '.txt' files are allowed."}), 400

        data = file.read().decode('utf-8')
        logger.info("File read successfully")
        
        # JSON 데이터 변환
        try:
            parsed_data = json.loads(data)
            logger.info("JSON parsed successfully")
        except JSONDecodeError as e:
            logger.warning(f"Invalid JSON format: {str(e)}")
            return jsonify({"error": "Invalid JSON format"}), 400

        # 반환할 데이터 가공하기
        [return_keyword, sentiment_dict] = process_received_data(parsed_data, tokenizer, ort_session, okt)
        logger.info("Data processed successfully")

        # 성공 응답 반환
        return jsonify({
            "pos" : return_keyword,
            "sentiment" : sentiment_dict
        }), 200
    
    except Exception as e:
        # 상세한 서버 오류 로그 출력
        logger.error("Unexpected error occurred", exc_info=True)
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

