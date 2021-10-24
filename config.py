import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    API_KEY = os.environ.get('Stock_Key')
    SECRET_KEY = os.environ.get('SECRET_KEY')

#To enable developement environment on PS($env:FLASK_ENV="developement")
#To enable DEBUG on PS($env:FLASK_DEBUG=1)