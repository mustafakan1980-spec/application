#!/bin/bash
python3.12 -m pip install -r requirements.txt --break-system-packages || pip install -r requirements.txt --break-system-packages || uv pip install -r requirements.txt --system
python3.12 manage.py collectstatic --no-input --clear || python manage.py collectstatic --no-input --clear
