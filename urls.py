from deanthe import url
from apps.cyber.views import cyber_index

url('/', 'cyber_index', cyber_index)
