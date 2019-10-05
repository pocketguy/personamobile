FROM python:3.7.4-alpine3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.10/main > /etc/apk/repositories \
  && echo http://mirror.yandex.ru/mirrors/alpine/v3.10/community >> /etc/apk/repositories \
  && apk --no-cache add \
  build-base \
  postgresql-dev \
  zlib-dev \
  jpeg-dev \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "gunicorn", "-c", "python:gunicorn_docker_config", "project.wsgi:application" ]
