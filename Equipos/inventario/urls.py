from django.urls import path
from . import views


urlpatterns = [
    path('<pk>', views.ImplementosDeportivosDetailView.as_view(), name='Deportivovista'), #id ---> llave primaria
    path('<pk>', views.RopaDetailView.as_view(), name='Ropavista')
]