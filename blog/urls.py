from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:name>', views.category_posts, name='category-posts'),
]
