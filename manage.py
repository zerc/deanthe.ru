from deanthe import app, manager

@manager.command
def runserver():
	""" Start the development server """
	app.run(host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
	manager.run()
