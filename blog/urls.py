from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:category_name>', views.posts, name='category-posts'),
    path('posts', views.posts, name='posts'),
]
