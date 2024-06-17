from django.urls import path
from . import views


urlpatterns = [
  path('', views.teams, name='teams'),
  path('team/<int:id>', views.team, name='team'),
]