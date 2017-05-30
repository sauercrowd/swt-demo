FROM python:3
WORKDIR /src/app

RUN pip install redis flask

COPY app.py /src/app
COPY templates /src/app/templates

EXPOSE 8080
CMD ["python","app.py"]
