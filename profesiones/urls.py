from django.urls import path
from . import views

urlpatterns = [
    path('licenciado/crear/', views.crear_licenciado, name='crear_licenciado'),
    path('licenciado/',views.lista_licenciado, name='lista_licenciado'),
]
