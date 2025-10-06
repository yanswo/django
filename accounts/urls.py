from django.urls import path
from .views import login_view, index, logout_view, home_view, gerencia_view, administrador_view, perfil_view

urlpatterns = [
    path('', index, name='index'),
    path('home/', home_view, name='home'),
    path('gerencia/', gerencia_view, name='gerencia'),
    path('administrador/', administrador_view, name='administrador'),
    path('perfil/', perfil_view, name='perfil'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]