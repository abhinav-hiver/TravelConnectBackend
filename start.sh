#!/bin/bash
# Running migrations

set -e

. .venv/bin/activate
alembic upgrade head
# if [ $? -ne 0 ]; then
#     echo 'Error in running database migrations'> server_uvicorn.log
#     exit 1
# fi
# .venv/bin/uvicorn src:app --host 0.0.0.0 --port 80 --reload --log-level info > server_uvicorn.log

python server.py