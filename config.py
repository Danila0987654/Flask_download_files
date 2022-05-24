from dotenv import load_dotenv
import os

load_dotenv()

class Config():

    _true_values = ['yes', 'y', 'true', '1']

    FLASK_HOST = os.getenv("HOST")
    FLASK_PORT = os.getenv("PORT")
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv("DEBUG").lower() in _true_values
    SECRET_KEY = os.getenv("SECRET_KEY")
