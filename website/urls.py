from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('mainframe.html', views.mainframe, name='mainframe')
]
