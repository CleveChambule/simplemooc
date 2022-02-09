from django.urls import path
from  . import  views


urlpatterns = [
    path('', views.cursos, name='cursos'),
    #path("details", views.contacto, name='contact')
]