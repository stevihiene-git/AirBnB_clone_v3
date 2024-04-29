#!/usr/bin/python3

"""my flas application """
from flask import Flask, Blueprint, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views



app = Flask(__name__)
app.register_blueprint(app_views,url_prefix='/api/v1' )



@app.errorhandler(404)
def not_found(error):
        """ 404 Error 
        ---responses:
            404:
            description: a resource was not found
            """
            return make_response(jsonify({'error': "Not found"}), 404)



@app.teardown_appcontext
def teardown_appcontext(error):
    """remove app_context session """
    storage.close()


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True")

