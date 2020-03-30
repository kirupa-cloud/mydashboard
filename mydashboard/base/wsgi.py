"""
WSGI config for mydashboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""



from django.core.wsgi import get_wsgi_application
from .utils import get_os_environ

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydashboard.settings')

get_os_environ('DJANGO_SETTINGS_MODULE')

application = get_wsgi_application()
