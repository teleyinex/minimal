import os
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

import settings_local as settings

def configure_app(app):
    app.config.from_object(settings)
    app.config.from_envvar('PYBOSSA_SETTINGS', silent=True)
    # parent directory
    here = os.path.dirname(os.path.abspath( __file__ ))
    config_path = os.path.join(os.path.dirname(here), 'settings_local.py')
    if os.path.exists(config_path):
        app.config.from_pyfile(config_path)

@app.context_processor
def global_template_context():
    return dict(
         brand = app.config['BRAND'],
         title = app.config['TITLE'],
         copyright = app.config['COPYRIGHT'],
         description = app.config['DESCRIPTION'],
         herounit = app.config['HEROUNIT'],
         carousel = app.config['CAROUSEL'],
         year = datetime.now().year
         )

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    configure_app(app)
    app.run()
