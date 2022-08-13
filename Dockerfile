FROM python:3.9.13-slim

RUN pip install -U pip
RUN pip install -r requrements.txt

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]