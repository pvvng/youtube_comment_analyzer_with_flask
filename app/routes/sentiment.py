# flask
from flask import request, jsonify, Blueprint
import json

# 데이터 처리 함수
from app.utils.my_functions.process_received_data import process_received_data
# 형태소 분석
from konlpy.tag import Okt
# sentiment 모델 불러오기
import onnxruntime as ort
# import numpy as np
from transformers import AutoTokenizer
# 시간 재기
import time

# 블루프린트 정의
sentiment_bp = Blueprint('sentiment', __name__)

# okt 객체 생성
okt = Okt()

# 변환된 ONNX 모델 로드
ort_session = ort.InferenceSession("app/models/kcbert_model.onnx")
model_path = "app/models/models-steam-fp16"

# 토크나이저만 가져오고, PyTorch 없이 추론
tokenizer = AutoTokenizer.from_pretrained(model_path)

# POST 요청을 처리할 API 엔드포인트
@sentiment_bp.route('/receive_data', methods=['POST'])
def receive_data():
    try:
        # 받은 파일 댓글 데이터 변환
        file = request.files['file']
        data = file.read().decode('utf-8')
        
        # 받은 데이터 딕셔너리로 변환
        parsed_data = json.loads(data)

        # 시작시간  
        start_time = time.time()
        print("Data received and parsed successfully")  # 디버깅 출력

        # log 출력
        print("pending...")

        # 반환할 데이터 가공하기
        [return_keyword, sentiment_dict] = process_received_data(parsed_data, tokenizer, ort_session, okt)
        
        end_time = time.time()
        ex_time = end_time - start_time
        # 소요시간 출력
        print(f"소요시간 :{ex_time}")

        # 성공 응답 반환
        return jsonify({
            "pos" : return_keyword,
            "sentiment" : sentiment_dict
        }), 200
    
    except Exception as e:
        print("Error:", str(e))  # 에러 메시지 출력
        return jsonify({"error": str(e)}), 500
