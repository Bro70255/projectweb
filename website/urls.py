from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mainframe/', views.mainframe, name='mainframe'),
    path('contact/', views.contact, name='contact'),
    path('about/',views.about,name='about')
]
