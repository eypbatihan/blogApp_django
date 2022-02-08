from django.urls import path
from .views import post_create, post_list


urlpatterns = [
    path("post_create/",post_create,name='create'),
    path('post_list/',post_list,name='list'),
]
