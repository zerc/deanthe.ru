from deanthe import url
from apps.cyber.views import cyber_index
from apps.accounts.views import accounts_login

url('/', 'cyber_index', cyber_index)

url('/login', 'accounts_login', accounts_login, methods = ['GET', 'POST']);
