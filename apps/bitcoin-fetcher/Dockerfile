FROM python:3.9

WORKDIR ~/app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT flask run --host 0.0.0.0