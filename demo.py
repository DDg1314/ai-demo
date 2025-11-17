# demo.py —— 通用中文情感分析
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="LiYuan/amazon-review-sentiment-analysis",
    tokenizer="LiYuan/amazon-review-sentiment-analysis",
    return_all_scores=False
)

text = "深圳的AI岗位真多！"
result = classifier(text)
print(f"文本: {text}")
print(f"情感: {result[0]['label']} (置信度: {result[0]['score']:.4f})")