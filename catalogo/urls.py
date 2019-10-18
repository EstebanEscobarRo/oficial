from django.urls import path
from . import views

urlpatterns = [

    #Llamada al método index creado en views.
    path('',views.index,name='index'),

]