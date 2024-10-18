# 키워드 후처리 함수 호출
from app.utils.my_functions.process_keyword import process_keyword

def get_keyword(okt, data) :
    # 형태소 분리
    pos_result = okt.pos(data)

    # 기존 댓글 split
    splited_sentence = data.split()

    # 키워드 배열 생성
    keyword = process_keyword(splited_sentence, pos_result)
    return keyword
