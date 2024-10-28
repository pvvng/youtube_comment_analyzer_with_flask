
from scipy.special import softmax

# 예측 함수 정의
def predict_sentiment(text, tokenizer, ort_session):
    # 토크나이저를 사용해 ONNX Runtime에 맞는 입력 생성
    inputs = tokenizer(text, return_tensors="np")["input_ids"]
    ort_inputs = {"input_ids": inputs}
    
    # ONNX Runtime을 사용하여 추론 수행
    logits = ort_session.run(None, ort_inputs)[0]

    # 소프트맥스를 사용하여 확률 값 계산
    probabilities = softmax(logits, axis=1)
    positive_confidence = probabilities[0, 1]  # 긍정 확률

    # 중립 임계값 설정 (예시로 70% 이상을 긍/부정, 그 외는 중립으로 설정)
    if 0.4 < positive_confidence < 0.6:
        return "neutral"
    elif positive_confidence >= 0.6:
        return "positive"
    else:
        return "negative"
