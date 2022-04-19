#!/usr/bin/env bash
while true; do
  echo "Re-starting Django runserver - For Developement"
  python manage.py runserver 0.0.0.0:8000
  sleep 2
done