from flask import Flask
from os.path import join, split

app = Flask(__name__)
app.root_path = '/'.join(app.root_path.split('/')[:-1])
app.config.from_object('deanthe.config.DevelopmentConfig')
