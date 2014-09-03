from deanthe import db
from hashlib import md5

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(32), unique = True)
	nickname = db.Column(db.String(24))
	password = db.Column(db.String(32))
	role = db.Column(db.String(24))

	def __init__(self, email, nickname, password, role = 'user'):
		self.email = email
		self.nickname = nickname
		self.password = self.__hash_password(password)
		self.status = status
		self.role = role

	def __hash_password(self, password):
		return md5(password.encode()).hexdigest()

	def check_password(self, password):
		return True if self.password == self.__hash_password(password) else False
