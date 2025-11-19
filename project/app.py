# project/app.py

# ========== 关键修复：绕过 matplotlib ==========
import gradio.utils
gradio.utils.MatplotlibBackendMananger = lambda: gradio.utils.DummyContext()
gradio.utils.DummyContext = type("DummyContext", (), {
    "__enter__": lambda s: None,
    "__exit__": lambda s, *a: None
})
# ============================================

import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

# 加载模型
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def predict(text):
    if not text or not text.strip():
        return "请输入有效文本"
    try:
        inputs = tokenizer(text.strip(), return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
            label_id = torch.argmax(outputs.logits, dim=-1).item()
        return {0: "负面", 1: "中性", 2: "正面"}.get(label_id, f"标签{label_id}")
    except Exception as e:
        return f"错误: {str(e)}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=2, placeholder="输入英文描述，如: I have a headache"),
    outputs="text",
    title="深圳AI医疗助手（修复版）",
    description="已绕过 matplotlib 冲突，纯文本情感分析。",
    examples=[
        ["I feel great!"],
        ["Headache and nausea"],
        ["Worried about test results"]
    ]
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)