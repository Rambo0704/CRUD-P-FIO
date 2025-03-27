from app_pifio import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('pifios/', views.criar_pifio, name='pifios'),
    path('tabela/', views.criar_tabela, name='tabela'),
]
