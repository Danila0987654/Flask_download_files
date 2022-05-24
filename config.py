from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():

    _true_values = ['yes', 'y', 'true', '1']

    FLASK_HOST = os.getenv("HOST")
    FLASK_PORT = os.getenv("PORT")
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv("DEBUG").lower() in _true_values
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATA_DIR = os.path.join(BASE_DIR, os.getenv('DATA_DIR'))
