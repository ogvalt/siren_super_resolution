FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

# basic deps for python

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
         build-essential \
         cmake \
         ca-certificates \
         curl \
         python3.8 \
         python3.8-dev \
         python3.8-distutils \
         libglib2.0-0 \
         && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3.8 /usr/local/bin/python3 \
    && ln -s /usr/bin/pydoc3.8 /usr/local/bin/pydoc3 \
    && ln -s /usr/bin/python3.8-config /usr/local/bin/python3-config \
    && python3 --version

WORKDIR /setup

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip3 --version

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# install poetry

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py > get-poetry.py && \
    python3 get-poetry.py --yes

WORKDIR /env

# config runtime environment
COPY poetry.lock pyproject.toml  /env/

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction

WORKDIR /workspace



