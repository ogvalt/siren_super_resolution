#!/bin/bash

readonly SRC_PATH=$(dirname "$(realpath "$0")")
source "${SRC_PATH}/../set_env.sh"

docker build -t "$PROJECT_NAME":latest \
             -f "$PROJECT_PATH"/docker/Dockerfile \
             "$PROJECT_PATH"


