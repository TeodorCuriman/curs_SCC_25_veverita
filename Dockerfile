FROM python:3.10-slim

# Instalare dependențe necesare pentru pygame
RUN apt-get update && apt-get install -y \
    libsdl2-mixer-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-ttf-2.0-0 \
    && apt-get clean

# Instalare pygame prin pip
RUN pip install pygame

# Creează un director de lucru
WORKDIR /app

# Copiază toate fișierele în container
COPY . .

# Rulează aplicația
CMD ["python", "main.py"]
