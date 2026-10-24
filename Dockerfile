FROM python:alpine3.12
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        python3-dev \
        libffi-dev \
    && apk add --no-cache \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev
# RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf
RUN apk add --no-cache g++

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn
# COPY ./ ./

RUN apk del .build-deps
ENTRYPOINT ["/bin/sh", "startup.sh"]