#!/bin/bash

set -o errexit
set -o pipefail

readonly SRC_PATH=$(dirname "$(realpath "$0")")
source "${SRC_PATH}/../set_env.sh"

# TODO: meaningful port exposure

container_setup="--rm -it --name ${PROJECT_NAME} ${PROJECT_NAME}:latest bash"

docker run "${DOCKER_RUNTIME}" "${container_setup}"
