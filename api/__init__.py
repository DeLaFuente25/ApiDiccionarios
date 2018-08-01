from flask import Flask
from settings import DevelopmentConfig
from models import db


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
with app.app_context():
    db.create_all()
