### 
# import os
"""from dotenv import load_dotenv

load_dotenv()

class Config(object):
    #Base Config Object
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = 'b08edcc51fe869'
    MAIL_PASSWORD = '3450a13bce11dc'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False