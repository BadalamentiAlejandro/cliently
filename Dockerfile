FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y dos2unix curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir -r requirements.txt

COPY . .

RUN dos2unix ./entrypoint.sh && chmod +x ./entrypoint.sh
RUN dos2unix ./wait-for-it.sh && chmod +x ./wait-for-it.sh

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000