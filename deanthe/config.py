class Config(object):
	DEBUG = False
	TESTING = False

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database/db.sqlite3'
