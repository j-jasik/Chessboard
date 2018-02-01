from flask import Flask
app = Flask(__name__)

from app.views import BaseView
BaseView.register(app)