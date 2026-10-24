#!/bin/bash

# python sid_server.py
# gunicorn -b 0.0.0.0:5000 --log-level debug sid_server:app
# gunicorn -h
gunicorn -b 0.0.0.0:5000 -w 2 --access-logfile - --threads 4 --log-level debug 'flaskr:create_app()'