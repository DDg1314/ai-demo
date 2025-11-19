# app.py
from transformers import pipeline

# 使用一个真实微调过的情感分析模型（英文）
classifier = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def predict(text):
    result = classifier(text)
    return result[0]['label']

# 测试（用英文，因为模型是英文的）
test_inputs = [
    "I have a headache",          # 应该偏负面
    "Feeling great today!",       # 正面
    "Coughing all night",         # 负面
    "The medicine worked well",   # 正面
    "Fever won't go down"         # 负面
]

for text in test_inputs:
    print(f"输入: {text} → 分类: {predict(text)}")