# Temel imaj olarak Python'ın Alpine Linux tabanlı 3.12 sürümünü kullan
FROM python:3.12-slim

# Çalışma dizinini /app olarak ayarla
WORKDIR /app

# requirements.txt dosyasını çalışma dizinine kopyala
COPY requirements.txt .

# requirements.txt dosyasında belirtilen bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# app.py dosyasını çalışma dizinine kopyala
COPY app.py .

# Uygulamanın 7860 numaralı portu dinleyeceğini Docker'a bildir
EXPOSE 7860

# Uygulamayı başlatmak için çalıştırılacak komut
CMD ["python", "app.py"]