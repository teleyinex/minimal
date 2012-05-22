# Activate the virtual env
activate_this = '/home/teleyinex/Proyectos/public_html/minimal/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# Import sys to add the path of minimal 
import sys
sys.path.insert(0,'/home/teleyinex/Proyectos/minimal')
# Run the web-app
from minimal.app import app as application
application.debug = True
