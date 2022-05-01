from django.urls import path
from poll import views as poll_views

urlpatterns = [
    path('', poll_views.home, name='home'),
    path('create/', poll_views.create, name='create'),
    path('vote/<str:pk>/', poll_views.vote, name='vote'),
    path('results/<str:pk>/', poll_views.results, name='results'),
]