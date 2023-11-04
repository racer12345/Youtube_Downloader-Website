import os

from flask import Flask

form .config import Config

app = Flask(__name__)

app.config.from_object( Config )

from app import views