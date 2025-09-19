import gradio as gr
from transformers import pipeline
import sys # Hata yakalamak için sys modülünü ekledik

# Küçük ve hızlı bir duygu analizi modeli yükle
# Bu model ilk çalıştığında indirilecektir.
try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    print("Duygu analizi modeli başarıyla yüklendi.")
except Exception as e:
    print(f"UYGULAMA BAŞLATILIRKEN MODEL YÜKLEME HATASI: {e}", file=sys.stderr)
    sys.exit(1)

def analyze(text: str):
    text = (text or "").strip()
    if not text:
        return "⚠️ Lütfen kısa bir metin girin."

    # Metnin duygu analizini yap
    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    if label == "POSITIVE":
        # Olumlu duygu ise emoji ve puanı göster
        return f"🎉 [Label: {label}, Score: {score:.2f}]"
    else:
        # Olumsuz duygu ise emoji ve puanı göster
        return f"😟 [Label: {label}, Score: {score:.2f}]"

# Gradio arayüzünü oluştur
demo = gr.Interface(
    fn=analyze, # Kullanılacak Python fonksiyonu
    inputs=gr.Textbox(lines=4, label="Metin"), # 4 satırlık metin kutusu girişi
    outputs="text", # Çıktının metin olacağını belirtir
    title="Hafif LLM: Duygu Analizi", # Uygulamanın başlığı
    description="Kısa metinlerde hızlı duygu analizi (DistilBERT).",
    examples=[["I absolutely loved this film!"], ["This was painfully boring..."]] # Örnek girdiler
)

# Uygulamayı başlat
try:
    print("Gradio uygulaması başlatılmaya çalışılıyor...")
    demo.launch(server_name="0.0.0.0", server_port=7860)
except Exception as e:
    print(f"UYGULAMA BAŞLATILIRKEN BİR HATA OLUŞTU: {e}", file=sys.stderr)
    sys.exit(1)


