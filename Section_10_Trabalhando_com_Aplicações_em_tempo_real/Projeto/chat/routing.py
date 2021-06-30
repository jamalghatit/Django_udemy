from django.urls import re_path # cria path com expressoes regulares

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer.as_asgi()),
]


# ws -> websocket
