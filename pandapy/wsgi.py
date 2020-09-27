import os, sys 

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/cesarpimentajs/pandapy')
sys.path.append('/home/cesarpimentajs/venv/Lib/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandapy.settings')

application = get_wsgi_application()
