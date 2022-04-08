FROM python:3-slim

WORKDIR /app

COPY requirements.txt ${WORKDIR}

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY listener.py ${WORKDIR}

ENTRYPOINT ["python", "listener.py"]
