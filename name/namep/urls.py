from django.urls import path 
from . import views

app_name = 'namep'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/put', views.put, name='put'),
    path('<int:id>/delete', views.delete, name='delete'),


]