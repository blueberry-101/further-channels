"""
ASGI config for redissite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

# Channels Configrations
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter , ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator
from mylayer.routes import websocket_urlpatterns
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redissite.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http" : asgi_application,
    "websocket" : URLRouter(websocket_urlpatterns)
})
