#!/bin/bash

readonly SRC_PATH=$(dirname "$(realpath "$0")")
source "${SRC_PATH}/set_env.sh"

# check dependencies

command -v wget >/dev/null 2>&1 || { echo >&2 "I require wget but it's not installed.  Aborting."; exit 1; }
command -v unzip >/dev/null 2>&1 || { echo >&2 "I require unzip but it's not installed.  Aborting."; exit 1; }
command -v busybox >/dev/null 2>&1 || { echo >&2 "I require busybox but it's not installed.  Aborting."; exit 1; }

DEST="$(realpath "$PROJECT_PATH"presets/data/)"

train_dest="$DEST"/LapSRN/train/ && mkdir -p "$train_dest"
test_dest="$DEST"/LapSRN/train/ && mkdir -p "$test_dest"

echo "Starting dataset download, saving into: ""$DEST"""
wget -qO- http://vllab.ucmerced.edu/wlai24/LapSRN/results/SR_training_datasets.zip |
    busybox unzip - -d "$DEST"/LapSRN/train/

wget -qO- http://vllab.ucmerced.edu/wlai24/LapSRN/results/SR_testing_datasets.zip |
    busybox unzip - -d "$DEST"/LapSRN/test/




