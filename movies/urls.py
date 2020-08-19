from django.urls import path
from django.contrib import admin
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('admin/', admin.site.urls, name='adminpanel'),

]
