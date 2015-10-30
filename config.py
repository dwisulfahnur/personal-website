'''Configuration File'''
import os

#Development (Debug => True)0
DEBUG = True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLITE
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_DIR, 'app.db')
