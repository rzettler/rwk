#!/bin/bash

echo port is "$VCAP_APP_PORT"   
which python
pwd
python manage.py migrate   
python manage.py runserver --noreload 0.0.0.0:$VCAP_APP_PORT   