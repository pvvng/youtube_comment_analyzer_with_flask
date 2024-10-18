# flask
from flask import request, jsonify, Blueprint
import json

# 데이터 처리 함수
from app.utils.my_functions.process_received_data import process_received_data
# 형태소 분석
from konlpy.tag import Okt
# sentiment 모델 불러오기
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
# 시간 재기
import time

# 블루프린트 정의
sentiment_bp = Blueprint('sentiment', __name__)

# okt 객체 생성
okt = Okt()

model_path = "./models-steam-fp16"

# 로컬 경로에서 KcBERT 모델과 토크나이저 로드
v4_tokenizer = AutoTokenizer.from_pretrained(model_path)
v4_model = AutoModelForSequenceClassification.from_pretrained(model_path)

# POST 요청을 처리할 API 엔드포인트
@sentiment_bp.route('/receive_data', methods=['POST'])
def receive_data():

    # 받은 파일 댓글 데이터 변환
    file = request.files['file']
    data = file.read().decode('utf-8')

    # 받은 데이터 딕셔너리로 변환
    parsed_data = json.loads(data)

    # 시작시간  
    start_time = time.time()

    # log 출력
    print("pending...")

    # 반환할 데이터 가공하기
    [return_keyword, sentiment_dict] = process_received_data(parsed_data, v4_tokenizer, v4_model, okt, F)

    end_time = time.time()
    ex_time = end_time - start_time
    # 소요시간 출력
    print(f"소요시간 :{ex_time}")

    # 성공 응답 반환
    return jsonify({
        "pos" : return_keyword,
        "sentiment" : sentiment_dict
    }), 200