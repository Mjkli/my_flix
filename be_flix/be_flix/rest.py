
# file that will control the main backend
# should start a main thread that will control a veriaty of different services
# File browsing server that will display info regarding video files
# Rest server that will take API commands from the frontend
# Websocket service that will start only when called from the REST API

import json
import websockets
import socket
from flask import Flask

app = Flask(__name__)

class RestServer():
    def __init__(self):
        self.app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index(self):
        return json.dumps({'item': 1})

    @app.route('/get_port', methods=['GET'])
    def get_port(self):
        return json.dumps({'print': "get_port"})

    @app.route('/request_websocket', methods=['GET'])
    def get_websocket(self):
        # start websocket thread to interactwith and close after use
        return json.dumps({})


def rest_server():
    rest = RestServer()
    rest.app.run(debug=True)

if __name__ == '__main__':
    rest_server()


