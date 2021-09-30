from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('KM_draw', views.draw),
]