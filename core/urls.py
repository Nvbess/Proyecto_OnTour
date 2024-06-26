from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("index/", index, name="index"),
    path("contrato/", contrato, name="contrato"),
    path("listar/", listarContrato, name="listar"),
    path("ver-contrato/<int:id>/", verContrato, name="ver-contrato"),
    # Login/Logout
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]