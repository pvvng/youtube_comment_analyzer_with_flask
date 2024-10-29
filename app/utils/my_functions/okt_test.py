# 형태소 분석
from konlpy.tag import Okt

# okt 객체 생성
okt = Okt()

origin_text = "구글한테 망사용료로 뭐라 못하는게 코미디넼ㅋㅋㅋ"
result = okt.pos(origin_text);

print(origin_text)
print(result)