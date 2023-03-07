from django.urls import path, re_path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.create_menu, name='create_menu'),
    re_path(r'^genres/$', views.index, name='index'),
]