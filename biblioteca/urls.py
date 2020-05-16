from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('registrarse/', views.registro, name='registro'),
    path('listado/', views.index, name='index'),
    path('detalle/<str:tipo>/<int:pk>/', views.detalle, name='detalle'),
    path('get-reservar/<int:pk>/', views.get_reserva, name='reservar'),
    path('reservar', views.reservar, name='reservar'),
    path('logout/', views.logout, name='logout'),
]
