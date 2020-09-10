from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('update', views.update),
    path('delete', views.deleteUser)
]
