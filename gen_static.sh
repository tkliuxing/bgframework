#!/bin/bash

./manage.py collectstatic --noinput
./manage.py assets build
cp static/bgframework/packed.* src/bgframework/static/bgframework/