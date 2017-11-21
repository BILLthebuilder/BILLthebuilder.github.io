# app/__init__.py

from flask import Flask

# We now Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Loading the views
from app import views

# Loading the config file
app.config.from_object('config')