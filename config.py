import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

#Gives access to the project in ANY OS we find
#Allows outside files/folder to ne added to the project
#from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
                SET Config variables for the flask app.
                Using enviromentt variables where available others
                create the config variable if not done already.

    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or ' You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
#     FLASK_APP = os.environ.get('FLASK_APP')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages from sqlalchemy