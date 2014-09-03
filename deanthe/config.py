class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = 'secret_key' 

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database/db.sqlite3'
