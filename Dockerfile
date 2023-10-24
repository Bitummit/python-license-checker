FROM python:3.11

ENV PYTHONUNBUFFERED=1

COPY . /opt/

# RUN echo 'alias python_checker="python /opt/start.py"' >> -/.bashrc
RUN echo -e '#!/bin/bash\npython /opt/start.py "$@"' > /usr/bin/python_checker && chmod +x /usr/bin/python_checker

CMD ["python", "/opt/start.py"]
