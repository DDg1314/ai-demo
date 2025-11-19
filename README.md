  AI Demo


   1: 调用情感分析模型

   “由于缺乏公开医疗意图分类模型，本 Demo 使用通用情感模型演示 pipeline 流程。实际医疗系统需在合规数据上微调。”
   <img width="2036" height="1142" alt="ScreenShot_2025-11-19_094831_618" src="https://github.com/user-attachments/assets/e50e7908-1d05-4922-8a08-4aaed8255cdc" />



   2: 情感分析 Web Demo
使用 Gradio 构建交互界面，基于 Hugging Face 预训练情感模型。
注意：模型为英文通用情感分析，非医疗诊断工具。
<img width="2546" height="1352" alt="ScreenShot_2025-11-19_103849_543" src="https://github.com/user-attachments/assets/bc41d0e3-78c7-40c8-b086-59261c4551ea" />



   3:AI应用链接，任何人都可以使用
   https://lyraen-medical-sentiment-demo.hf.space

总结:
 深圳AI医疗助手（情感分析 Demo）

> 基于预训练 Transformer 模型的情绪倾向分析演示系统  
> 注意：本项目不提供疾病诊断，仅用于技术流程展示

 技术栈
- Python, Transformers, Gradio
- 预训练模型: [`cardiffnlp/twitter-roberta-base-sentiment-latest`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
- 功能：输入健康相关文本 → 输出情绪倾向（正面 / 中性 / 负面）

 演示
在线体验: [https://lyraen-medical-sentiment-demo.hf.space](https://lyraen-medical-sentiment-demo.hf.space)

> 💡 建议输入英文描述，例如：
> - `"I have a headache"`
> - `"Feeling much better today!"`

 运行
```bash
pip install -r requirements.txt
python app.py

模型为通用情感分析模型，非医疗专用，对中文支持有限
实际医疗系统需在合规数据上微调专用分类模型
已绕过 matplotlib 依赖冲突，确保在无 GUI 环境（如腾讯云、Hugging Face Spaces）稳定运行
