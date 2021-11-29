FROM python:3.7.2-alpine3.8

EXPOSE 5321

RUN pip install flask

WORKDIR /opt
RUN mkdir src
RUN mkdir data

WORKDIR /opt/data
COPY /data .

WORKDIR /opt/src
COPY /src .
CMD ["python", "flask_it.py"]
