FROM python:3.6


ENV DIR /opt/flask-app
COPY ./requirements.txt $DIR/requirements.txt
WORKDIR  $DIR
RUN pip install -U --no-cache-dir pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt remove --purge && apt-get clean && \
    rm -rf /tmp/*


COPY . $DIR
ENV API_PORT 3000
EXPOSE $API_PORT


ENTRYPOINT ["sh", "./docker-entrypoint.sh"]