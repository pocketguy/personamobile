#!/bin/bash

set -eu

rand() {
    cat /dev/urandom | head -c 24 | base64
}

echo -n "\
API_SECRET_KEY=$(rand)
DB_PASSWORD=$(rand)
STORAGE_ACCESS_KEY=$(rand)
STORAGE_SECRET_KEY=$(rand)
"