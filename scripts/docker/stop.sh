#!/bin/bash

readonly SRC_PATH=$(dirname "$(realpath "$0")")
source "${SRC_PATH}/../set_env.sh"

docker stop "$PROJECT_NAME"
