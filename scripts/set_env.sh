#!/bin/bash

set -o errexit
set -o pipefail

PROJECT_PATH=$(dirname "$(realpath "${BASH_SOURCE[0]}")")/../
DOTENV_FILE=$PROJECT_PATH/.env

if [ -f "$DOTENV_FILE" ]
then
  export $(cat "$DOTENV_FILE" | sed 's/#.*//g' | xargs)
fi

echo "[SET_ENV] Environment variables exported"

