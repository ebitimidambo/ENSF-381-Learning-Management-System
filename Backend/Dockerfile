FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir flask flask-cors

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0", "--port=5000"]