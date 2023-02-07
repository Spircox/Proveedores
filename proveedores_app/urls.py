from django.contrib import admin
from django.urls import path, include
from proveedores_app.views import *

urlpatterns = [

        path('index/', index, name="inicio"),
        path('signup/', signup, name="sign-up"),
        path('', signin, name="sign-in"),
        path('formulario_archivos/', formulario_archivos, name="form_archiv"),
        path('signout/', signout, name="sign-out")
    ]