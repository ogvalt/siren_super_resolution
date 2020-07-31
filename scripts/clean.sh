#!/bin/bash

find . -type d -name '.pytest_cache' -exec rm -rf {} \;
find . -type d -name '.benchmarks' -exec rm -rf {} \;
find . -type d -name 'outputs' -exec rm -rf {} \;
find . -type d -name '__pycache__' -exec rm -rf {} \;
find ./presets/logs -type d -name 'dev*' -exec rm -rf {} \;
find . -type f -name '*nohup*' -exec rm -rf {} \;