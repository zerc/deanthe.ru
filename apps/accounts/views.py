from apps.common import *
from apps.users.models import User
from flask import request, session, redirect, url_for, g

@templated('users/login.html')
def users_login():
	title = 'Авторизация'
	error = None
	err_msg = 'Неверный логин или пароль.'
	if request.method == 'POST':
		inputEmail = request.form['inputEmail']
		inputPassword = request.form['inputPassword']
		user = User.query.filter_by(email = inputEmail).first()
		if user:
			if user.check_password(inputPassword):
				session['user'] = user.id
				g.user = user
				return redirect(request.args.get('next') or url_for('users_login'))
			else:
				error = err_msg
		else:
			error = err_msg
	return dict(title = title, error = error)
