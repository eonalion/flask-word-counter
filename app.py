import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Result

@app.route("/")
def index():
    return "Hello User! Welcome to Flask counter example app."


@app.route("/<name>")
def hello_name(name):
    return f"Hello {name}"


if __name__ == '__main__':
    app.run()
