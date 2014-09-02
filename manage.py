from deanthe import app, manager, db

@manager.command
def runserver():
	""" Start the development server """
	app.run(host = '0.0.0.0', port = 5000)

@manager.command
def createdb():
	""" Create database """
	db.create_all()

@manager.command
def dropdb():
	""" Drop database """
	db.drop_all()
	
if __name__ == '__main__':
	manager.run()
