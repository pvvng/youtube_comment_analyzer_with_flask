# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# # 로컬 모델 경로 지정
# model_path = "./models-steam-fp16"

# # 토크나이저와 모델 로드
# v4_tokenizer = AutoTokenizer.from_pretrained(model_path)
# v4_model = AutoModelForSequenceClassification.from_pretrained(model_path)

# # 예제 입력 설정
# dummy_input = v4_tokenizer("예시 문장", return_tensors="pt")["input_ids"]

# # ONNX 변환
# torch.onnx.export(
#     v4_model, 
#     dummy_input, 
#     "kcbert_model.onnx",  # ONNX 모델 저장 경로
#     input_names=["input_ids"], 
#     output_names=["logits"], 
#     dynamic_axes={"input_ids": {0: "batch_size"}, "logits": {0: "batch_size"}}
# )

# print("ONNX 모델 변환 완료")
