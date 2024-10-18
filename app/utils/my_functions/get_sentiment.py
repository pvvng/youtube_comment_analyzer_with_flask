# 감성 분석 함수
def get_sentiment(data, tokenizer, model, F):
    # 문장을 토큰화
    inputs = tokenizer(
        data, 
        return_tensors="pt",  # PyTorch 텐서 반환
        truncation=True,
        padding=True
    )

    # 모델을 사용해 감정 분석 수행
    outputs = model(**inputs)
    logits = outputs.logits

    # Softmax 함수 적용하여 확률 계산
    probs = F.softmax(logits, dim=1)

    # 확률을 백분율로 변환
    negative_prob = probs[0][0].item() * 100  # 부정일 확률
    positive_prob = probs[0][1].item() * 100  # 긍정일 확률

    # print(f'모델 {type} 분석 결과 : ', positive_prob, negative_prob)

    # # 긍정 부정 차이 계산
    diff = abs(positive_prob - negative_prob)
    if (diff <= 10):
        return "neutral"
    elif positive_prob > negative_prob :
        return "positive"
    else :
        return "negative"
