import gradio as gr
from transformers import pipeline

# Küçük ve hızlı bir sentiment modeli
clf = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)


def analyze(text: str):
    text = (text or "").strip()
    if not text:
        return "⚠️ Lütfen kısa bir metin girin."
    out = clf(text)[0]  # {'label': 'POSITIVE'/'NEGATIVE', 'score': ...}
    emo = "😊" if out["label"] == "POSITIVE" else "😞"
    return f"{emo} {out['label']} (güven: {out['score']:.2f})"


demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=4, label="Metin"),
    outputs=gr.Textbox(label="Sonuç"),
    title="Hafif LLM: Duygu Analizi",
    description="Kısa metinlerde hızlı sentiment (DistilBERT).",
)

# Yerelde tarayıcıdan ulaşmak için:
demo.launch(server_name="0.0.0.0", server_port=7860)


