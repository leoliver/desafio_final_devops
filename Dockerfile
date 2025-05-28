FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

run pip install -r requirements.txt

COPY . .

EXPOSE 1313

CMD ["python", "app.py"]