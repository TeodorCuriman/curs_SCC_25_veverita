FROM python:3.10-slim

# Instalare pachet necesar pentru pygame
RUN apt-get update && apt-get install -y \
    libsdl2-mixer-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-ttf-2.0-0 \
    python3-pygame \
    && apt-get clean

# Creează un director de lucru
WORKDIR /app

# Copiază toate fișierele în container
COPY . .

# Rulează aplicația
CMD ["python", "main.py"]

