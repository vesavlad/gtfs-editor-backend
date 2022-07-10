FROM python:3.8-alpine3.15 as base

FROM base as builder

RUN mkdir /install
COPY requirements.txt /install/requirements.txt
RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev geos-dev && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --no-warn-script-location --prefix /install -r /install/requirements.txt

FROM base

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY --from=builder /install /usr/local

WORKDIR /app

RUN apk update && apk add --no-cache openjdk11 postgresql-dev geos && \
    mkdir ./static && \
    mkdir ./media

# copy project files on /app folder
COPY . .

EXPOSE 8000
ENTRYPOINT ["/bin/sh", "docker/entrypoint.sh"]