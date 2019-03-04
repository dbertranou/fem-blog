from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category_posts/<str:name>', views.category_posts, name='category_posts'),
]
