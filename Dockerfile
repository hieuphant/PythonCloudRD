FROM python:alpine3.7
#install curl, jq for healthcheck.sh
# RUN apk add curl jq
COPY ./src/requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install --upgrade pip \
 && pip install -r requirements.txt
COPY ./src /src
# ENTRYPOINT sh healthcheck.sh