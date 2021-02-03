from flask import Flask, render_template
from flask_restplus import Api
from flask_cors import CORS

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        CORS(self.app)
        self.api = Api(self.app,
            version = '1.0',
            title = 'Apple Tree API',
            doc = '/docs',
            default='Métodos',
            default_namespace='')
        

    def run(self, ):
        self.app.run(
            debug=True
        )
            
server = Server()