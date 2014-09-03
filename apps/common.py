from deanthe import app
from functools import wraps
from flask import request, render_template, g, session

@app.before_request
def load_user():
	from apps.accounts.models import User
	g.user = User.query.filter(User.id == session['user']).first() if 'user' in session else None

def templated(template = None):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			template_name = template
			if template_name is None:
				template_name = request.endpoint.replace('.', '/') + '.html' 
			ctx = f(*args, **kwargs)
			if ctx is None:
				ctx = {}
			elif not isinstance(ctx, dict):
				return ctx
			return render_template(template_name, **ctx)
		return decorated_function
	return decorator

def is_admin(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user.role != 'admin':
			return redirect(url_for('accounts_login'))
		return f(*args, **kwargs)
	return decorated_function
	
def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			return redirect(url_for('accounts_login'))
		return f(*args, **kwargs)
	return decorated_function
