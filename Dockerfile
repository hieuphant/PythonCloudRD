FROM python:alpine3.7
COPY . /tmp
# COPY requirements.txt /tmp
WORKDIR /tmp

#install curl, jq for healthcheck.sh
# RUN apk add curl jq

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ENTRYPOINT sh healthcheck.sh
# CMD ["main.py"]