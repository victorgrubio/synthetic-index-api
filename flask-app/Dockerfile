FROM python:3.8.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV SQL_HOST sql
ENV SQL_PORT 3306

ENV DIR /opt/flask-app
COPY ./requirements.txt $DIR/requirements.txt
WORKDIR  $DIR
RUN pip install -U --no-cache-dir pip wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get update && apt-get -y dist-upgrade && apt-get install -y netcat && \
    apt remove --purge && apt-get clean && pip uninstall -y wheel && \
    rm -rf /tmp/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $DIR
ENV API_PORT 3000
EXPOSE $API_PORT


ENTRYPOINT ["sh", "docker-entrypoint.sh"]