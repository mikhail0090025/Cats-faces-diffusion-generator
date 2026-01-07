FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    gcc \
    python3-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && pip cache purge

RUN apt-get update && apt-get install -y tree curl && apt-get clean

COPY diffusion_model/ /app/
# RUN apt-get install -y curl && apt-get clean

USER root

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

CMD uvicorn endpoints:app --host 0.0.0.0 --port 5000