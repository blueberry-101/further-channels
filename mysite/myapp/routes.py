from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"wws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/(?P<room_name>\w+)/$", consumers.AsyncChatConsumer.as_asgi()),
]