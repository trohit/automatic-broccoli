#!/bin/bash

logger() {
    echo -e "`date +"%F %T.%6N"`: $1: $2"
}
# logger INFO hi
# 2025-02-08 08:54:28.297532: INFO: hi
