from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask_util_js import FlaskUtilJs


app = Flask(__name__)
db = SQLAlchemy(app)

fujs = FlaskUtilJs(app)

from app import views, models
