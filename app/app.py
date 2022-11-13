
from flask import Flask
# from database import database

# blueprint import
from apps.api.api import api
from apps.app1.views import app1
from apps.app2.views import app2

def create_app():
    app = Flask(__name__)

    # app.config.from_object('config.DevelopmentConfig')
    # database.init_app(app)

    # register blueprint
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(app1)
    app.register_blueprint(app2, url_prefix="/app2")
    
    return app

if __name__ == "__main__":
    create_app().run()
