import os

from dotenv import load_dotenv

load_dotenv()
if os.getenv('DEBUG').title() == 'True':
    DEBUG = True
elif os.getenv('DEBUG').title() == 'False':
    DEBUG = False

ENGINE = os.getenv('ENGINE')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
