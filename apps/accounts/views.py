﻿from apps.common import *
from apps.accounts.models import User
from flask import request, session, redirect, url_for, g, redirect

@templated('accounts/login.html')
def accounts_login():
	if g.user is not None:
		return redirect(url_for('cyber_index'))
	title = 'Авторизация'
	error = None
	err_msg_1 = 'Неверный логин или пароль.'
	if request.method == 'POST':
		inputEmail = request.form['inputEmail']
		inputPassword = request.form['inputPassword']
		user = User.query.filter_by(email = inputEmail).first()
		if user:
			if user.check_password(inputPassword):
				session['user'] = user.id
				g.user = user
				return redirect(request.args.get('next') or url_for('accounts_login'))
			else:
				error = err_msg_1
		else:
			error = err_msg_1
	return dict(title = title, error = error)
