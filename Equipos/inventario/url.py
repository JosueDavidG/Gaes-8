from django.urls import path
from . import views


urlpatterns = [
    path('<pk>', views.ImplementosDeportivosDetailView.as_view(), name='deportivo'), #id ---> llave primaria
    path('<pk>', views.ImplementosDeportivosDetailView.as_view(), name='deportivo')
]