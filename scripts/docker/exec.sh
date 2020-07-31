#!/bin/bash

readonly SRC_PATH=$(dirname "$(realpath "$0")")
source "${SRC_PATH}/../set_env.sh"

docker exec -it "$PROJECT_NAME" bash
