FROM python:3.9-buster

# RUN pwd
# RUN ps -la

COPY /requirements-old-2.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app .

CMD uvicorn view:app --host=0.0.0.0 --port=8000