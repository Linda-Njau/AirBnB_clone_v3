#!/usr/bin/python3

from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def close_storage(exception):
    storage.close()
    
if __name__ == "__main__":
    import os
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)

