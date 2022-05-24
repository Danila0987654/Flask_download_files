from flask import Flask
from config import Config

from app.routes.main import bp as main_bp


app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(main_bp)