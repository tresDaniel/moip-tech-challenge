FROM python:3.5.4
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt