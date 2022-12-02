"""myService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wedAviacion import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('registro/',views.registro,name='registro'),
    path('registroVuelo/',views.registroVuelo,name='registroVuelo'),
    path('consultaVuelo/',views.consultaVuelo,name='consultaVuelo'),
    path('bitacora/',views.bitacora,name='bitacora'),
    path('calendario/',views.calendario,name='calendario'),
    path('workshop/', views.workshop, name='workshop'),
    path('vistaAdmin/',views.vistaAdmin, name='vistaAdmin'),
    path('professionalPrograms/', views.professionalPrograms, name='professionalPrograms'),
    path('simulatorTraining/', views.simulatorTraining, name='simulatorTraining'),
    path('fullTimeTraining/', views.fullTimeTraining, name='fullTimeTraining'),
    path('admin/', admin.site.urls),
]
