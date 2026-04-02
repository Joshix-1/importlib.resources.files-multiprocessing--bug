#!/bin/sh

set -xeu

python3 -m badzip 0
python3 -m badzip 1
python3 -m badzip 10


python -m zipapp --compress --output badzip.pyz  --python "/usr/bin/env python3" badzip
chmod +x badzip.pyz
./badzip.pyz 0
./badzip.pyz 1
./badzip.pyz 10
