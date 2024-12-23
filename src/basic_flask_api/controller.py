import argparse
from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
import logging

from standalone_application import StandaloneApplication
from config import Config
from routes.tasks.task_routes import task_bp

app = Flask(__name__)

@app.get("/api/v1/swagger.json")
def swagger_spec():
    swag = swagger(app)
    swag["info"]["version"] = "0.0.0"
    swag["info"]["title"] = "Basic API Example"
    return jsonify(swag)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/api/docs",
    "/api/v1/swagger.json",
    config={
        "app_name": "Basic Flask API",
        "tryItOutEnabled": True
    }
)

app.register_blueprint(task_bp)
app.register_blueprint(swaggerui_blueprint)

# ===============================================================
def post_fork(server, worker):
    print("This is a custom post_fork function")
# ===============================================================


def main(config_path: str|None = None):

    if not config_path:
        parser = argparse.ArgumentParser(description="Basic Flask API")
        parser.add_argument("-c", "--config", help="Path to config file", required=True)

        args = vars(parser.parse_args())

        config_path = args["config"]


    config = None
    with open(config_path) as stream:
        config_yaml = yaml.safe_load(stream)

        port = int(config_yaml["port"])
        log_level = str(config_yaml["log_level"])
        num_workers = int(config_yaml["num_workers"])
        zombie_killer_sleep = int(config_yaml["zombie_killer_sleep"])
        
        config = Config(port, log_level, num_workers, zombie_killer_sleep)

    logging.basicConfig(level=config.log_level, format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    options = {
        'bind': '%s:%s' % ('0.0.0.0', config.port),
        'timeout': '120',
        'workers': config.num_workers,
        "post_fork": post_fork
    }
    StandaloneApplication(app, options, config.zombie_killer_sleep).run()

if __name__ == '__main__':
    main()