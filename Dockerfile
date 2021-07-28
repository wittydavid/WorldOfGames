FROM python:3.9-alpine

WORKDIR /app

COPY MainScores.py shared_func.py Utils.py scores.txt flask_app_req/requirements.txt .

COPY templates templates

RUN pip3 install -r requirements.txt

CMD [ "python3", "MainScores.py"]
