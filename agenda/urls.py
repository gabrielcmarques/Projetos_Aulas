from django.urls import path
from . import views as path_views

urlpatterns = [
    path('', path_views.home, name='home'),
    path('add/', path_views.addAgenda, name='add'),
    path('completar/<str:agenda_id>', path_views.completarTarefa, name='completar'),
    path('deletarcompleto/', path_views.deletarCompleto, name='deletarcompleto'),
    path('deletartudo/', path_views.deletarTudo, name='deletartudo'),
]
