FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir test_data
ADD ./static_templates.json /app/test_data/demo_templates.json
