import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    ENV = str(os.environ.get("ENV"))
    if ENV == "PROD":
        PROJECT_ID = str(os.environ.get("PROJECT_ID"))
        INSTANCE_NAME = str(os.environ.get("INSTANCE_NAME"))
        SQLALCHEMY_DATABASE_URI= f"mysql+mysqldb://root:{PASSWORD}@/{DATABASE}?unix_socket=/cloudsql/{PROJECT_ID}:us-central1:{INSTANCE_NAME}"
    else:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + \
        ':' + PASSWORD + '@' + HOST + '/' + DATABASE
        
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True