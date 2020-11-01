from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about,  name='about'),
    path('create', views.create, name='create')

]
