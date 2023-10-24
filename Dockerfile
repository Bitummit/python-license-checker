FROM python:3.11

ENV PYTHONUNBUFFERED=1

COPY . /opt/

RUN echo 'alias python_checker="python /opt/start.py"' >> -/.bashrc

CMD ["python", "/opt/start.py"]
