# File: main.py

from flask import Flask, jsonify
from flask_cors import CORS
from backend.api.routes import api
import logging

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register error handlers
    @app.errorhandler(Exception)
    def handle_error(error):
        logger.error(f"Unhandled error: {str(error)}")
        return jsonify({'error': str(error)}), 500
    
    app.register_blueprint(api, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)