"""Inititalize the flask app."""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask_flatpages import FlatPages

app = Flask(__name__, static_url_path="")
app.config.from_object('config')
pages = FlatPages(app)
db = SQLAlchemy(app)

from app import views, models

# end
