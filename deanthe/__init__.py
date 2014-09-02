from flask import Flask
from os.path import join, split
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.root_path = '/'.join(app.root_path.split('/')[:-1])
app.config.from_object('deanthe.config.DevelopmentConfig')

url = app.add_url_rule
manager = Manager(app)
db = SQLAlchemy(app)
