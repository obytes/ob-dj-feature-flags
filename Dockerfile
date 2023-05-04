FROM python:3.9.7-slim-buster

# prevent __pycache__ folder and files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN set -ex \
  && apt-get update \
  && apt-get install -qq -y --no-install-recommends \
  make \
  curl \
  gcc \
  git \
  jq \
  gettext \
  procps \
  python3-dev \
  sudo \
  postgresql-client \
  graphviz \
  vim \
  && pip install pipenv \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create appuser user for the application
RUN groupadd -g 9898 appuser && useradd -r -u 9898 -g appuser appuser -s /bin/bash
RUN usermod -aG sudo appuser
RUN mkdir /home/appuser && chown -R appuser /home/appuser
RUN mkdir /public_assets

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --dev --verbose

ADD . ./

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN chown -R appuser:appuser /public_assets
RUN chown -R appuser:appuser /app
RUN chown -R appuser:appuser /etc/environment
RUN echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER appuser
