# pull official base image
FROM python:3.10-slim

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install netcat-traditional && \
    apt-get -y install --no-install-recommends git curl libmagic1 libpq5 libpq-dev build-essential openssl libssl-dev libpango-1.0-0 libpangoft2-1.0-0 && \
    rm -rf /var/lib/apt/lists/*
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./app/ /code/
WORKDIR /code

ADD ./docker/app/entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
