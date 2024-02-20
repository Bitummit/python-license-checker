FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

COPY . /opt/

RUN echo 'python /opt/start.py "$@"' > /usr/bin/python_checker && chmod +x /usr/bin/python_checker

CMD ["/bin/bash"]
