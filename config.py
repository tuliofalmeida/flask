import os
 
class Config(object):
    SECRET_KEY = os.environ.get('SECREVT_KEY') or 'galado'
