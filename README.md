# Basic Flask API

## Basic Run (dev)
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

python3 src/controller.py -c etc/config.yaml
```
### Example startup logs
```
[2024-12-21 16:28:09 -0500] [15096] [INFO] Starting gunicorn 23.0.0
[2024-12-21 16:28:09 -0500] [15096] [INFO] Listening at: http://0.0.0.0:8082 (15096)
[2024-12-21 16:28:09 -0500] [15096] [INFO] Using worker: sync
[2024-12-21 16:28:09 -0500] [15097] [INFO] Booting worker with pid: 15097
[2024-12-21 16:28:09 -0500] [15098] [INFO] Booting worker with pid: 15098
[2024-12-21 16:28:09 -0500] [15099] [INFO] Booting worker with pid: 15099
[2024-12-21 16:28:09 -0500] [15100] [INFO] Booting worker with pid: 15100
[2024-12-21 16:28:09 -0500] [15101] [INFO] Booting worker with pid: 15101
```