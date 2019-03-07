from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:category_name>', views.posts, name='category-posts'),
    path('posts', views.posts, name='posts'),
    path('<slug:slug>', views.post_detail, name='post-detail'),
    path('api/filters', views.filter_list, name='filter-list'),
]
