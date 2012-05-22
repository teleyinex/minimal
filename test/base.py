from minimal import app
from minimal import settings_local as settings

webapp = app.app
webapp.config.from_object(settings)
webapp.config['TESTING'] = True
