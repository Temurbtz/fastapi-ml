FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update

COPY app /app

RUN pip install --upgrade pip && pip install -r /app/requirements.txt 

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]




