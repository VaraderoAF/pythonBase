import os

from flask import Flask
from flask_migrate import Migrate

from models import db
from views.cars import cars_app


app = Flask(__name__)
app.register_blueprint(cars_app, url_prefix="/cars")


CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)


db.init_app(app)


migrate = Migrate(app, db)


@app.route("/")
def root():
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
