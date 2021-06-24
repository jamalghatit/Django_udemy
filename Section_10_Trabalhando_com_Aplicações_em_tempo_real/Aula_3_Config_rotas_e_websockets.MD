# Configurando as Rotas e preparando para o WebSocket

criar o arquivo Section_10_Trabalhando_com_Aplicações_em_tempo_real\chat\urls.py:

```python
from django.urls import path

from .views import IndexView, SalaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala' ),
]
```

Criar o arquivo Section_10_Trabalhando_com_Aplicações_em_tempo_real\chat\routing.py:

```python
from django.urls import re_path # cria path com expressoes regulares

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$, ChatConsumer'),
]

# ws -> websocket
```

Em Section_10_Trabalhando_com_Aplicações_em_tempo_real\realtime\urls.py:

```python
from django.contrib import admin
from django.urls import path, include # add o include

urlpatterns = [
    path('', include('chat.urls')), # add
    path('admin/', admin.site.urls),
]
```

Criar o arquivo em Section_10_Trabalhando_com_Aplicações_em_tempo_real\realtime\routing.py:

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.routing import websocket_urlpatterns


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```
