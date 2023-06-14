"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from .views import apagarCadeira, apagarProjeto

app_name = "portfolio"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('javascript/', views.javascript, name='javascript'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('cadeiraNova/', views.cadeiraNova, name='cadeiraNova'),
    path('projetoNovo/', views.projetoNovo, name='projetoNovo'),
    path('editarCadeira/<int:cadeira_id>/', views.editarCadeira, name='editarCadeira'),
    path('editarProjeto/<int:projetos_id>/', views.editarProjeto, name='editarProjeto'),
    path('apagar-cadeira/<int:cadeira_id>/', apagarCadeira, name='apagarCadeira'),
    path('apagar-projeto/<int:projetos_id>/', apagarProjeto, name='apagarProjeto'),
    path('artigoNovo/', views.artigoNovo, name='artigoNovo'),
    path('comentarioNovo/', views.comentarioNovo, name='comentarioNovo'),

]
