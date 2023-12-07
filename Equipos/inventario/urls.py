from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>', views.ImplementosDeportivosDetailView.as_view(), name='Deportivovista'), #id ---> llave primaria
    path('<slug:slug>', views.RopaDetailView.as_view(), name='Ropavista')
]