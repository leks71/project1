from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('cat/<int:category_id>/', get_cat, name='cat'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]
