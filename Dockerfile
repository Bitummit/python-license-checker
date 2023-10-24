FROM python:3.11

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python", "start.py"]
