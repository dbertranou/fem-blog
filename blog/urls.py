from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<str:name>', views.categories, name='categories'),
]
