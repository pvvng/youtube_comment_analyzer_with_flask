# 감정 분석 함수 호출
from app.utils.my_functions.predict_sentiment import predict_sentiment
# 키워드 배열 반환함수 호출
from app.utils.my_functions.get_keyword import get_keyword
# 키워드 데이터 데이터 형식에 맞게 변형하는 함수 호출
from app.utils.my_functions.transform_keyword import transform_keyword
# 불용어 파일 호출
from app.utils.my_functions.stopword import stopword
# log 사용
import math

def process_received_data(parsed_data, tokenizer, ort_session, okt):

    # 반환할 js 객체 형태의 딕셔너리
    keyword_dict = {}
    sentiment_dict = {
        "positive" : 0,
        "negative" : 0,
        "neutral" : 0
    }

    for comment in parsed_data :
        text = comment['text']
        like = comment['like']
        # like 0 이하면 1로 변경
        if like <= 0:
            like = 1
        like_to_add = round(math.log2(like))
        # 좋아요 100 이하는 1로 변경 
        if like_to_add <= 0: 
            like_to_add = 1

        # 키워드 분석 결과 삽입
        keyword_result = []
        keyword_result.extend(get_keyword(okt, text))
        
        for keyword in keyword_result:
            # 공백 제거
            normalized_keyword = keyword.strip()
            if normalized_keyword not in stopword:
                if normalized_keyword in keyword_dict:
                    # 키워드가 이미 존재하면 기존 값에 추가
                    keyword_dict[normalized_keyword] += like_to_add
                else:
                    # 키워드가 존재하지 않으면 새로 추가
                    keyword_dict[normalized_keyword] = like_to_add
        
        # 감정 분석
        sentiment_result = predict_sentiment(text, tokenizer, ort_session)
        # 분석 결과 더하기 
        sentiment_dict[sentiment_result] += like_to_add

    # 종료시간  
    return_keyword = transform_keyword(keyword_dict)
    return [return_keyword, sentiment_dict]
