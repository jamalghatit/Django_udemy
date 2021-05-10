"""
WSGI config for fusion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')

application = Cling(MediaCling(get_wsgi_application()))

# dj_static é utilizado para apresentação de arquivos estáticos,
# O Cling é para arquivos estáticos e o MediaCling para apresentação de
# mídia, ou seja, arquivos de upload pelo usuário.