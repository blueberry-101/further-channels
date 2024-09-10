from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/<str:room_name>/",consumers.MyAWC.as_asgi(), name = "index"),
    path("jws/<str:room_name>/",consumers.MyJAWC.as_asgi())
]


''''
redis://default:eTgstqdKdBUHPpTvzSqjLrajxjgEusMa@redis.railway.internal:6379   // NOT WORKING!!

redis://default:eTgstqdKdBUHPpTvzSqjLrajxjgEusMa@autorack.proxy.rlwy.net:49704
'''