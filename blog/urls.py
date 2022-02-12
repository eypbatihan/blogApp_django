from django.urls import path
from .views import post_create, post_delete, post_list, post_update, post_details


urlpatterns = [
    path("post_create/", post_create, name='create'),
    path('post_list/', post_list, name='list'),
    path('post_details/<int:id>', post_details, name='details'),
    path('post_update/<int:id>', post_update, name='update'),
    path('post_delete/<int:id>', post_delete, name='delete'),
  
]
