from django.urls import path

from .views import IndexView, DadosJASONView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJASONView.as_view(), name='dados')
]