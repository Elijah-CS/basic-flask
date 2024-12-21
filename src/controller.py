import argparse
from flask import Flask, jsonify
import yaml

from standalone_application import StandaloneApplication
from config import Config

app = Flask(__name__)

@app.get("/api/v1/example")
def hello_world():
    return jsonify("Hello World!"), 200

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
        num_workers = int(config_yaml["num_workers"])

        config = Config(port, num_workers)

        

    options = {
        'bind': '%s:%s' % ('0.0.0.0', config.port),
        'workers': config.num_workers,
    }
    StandaloneApplication(app, options).run()

if __name__ == '__main__':
    main()