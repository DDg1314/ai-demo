# project/load_data.py
import os
from datasets import load_dataset
import pandas as pd

# 确保 project 目录存在
os.makedirs("project", exist_ok=True)

# 加载数据
dataset = load_dataset("pubmed_qa", "pqa_labeled")
df = pd.DataFrame(dataset["train"])

print(df.head())
print("总样本数:", len(df))

# 保存到 project/ 目录下
df.to_csv("project/pubmed_qa.csv", index=False)
print("✅ 数据已保存到 project/pubmed_qa.csv")