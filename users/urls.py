from blog.views import post_list
from users.views import  profile, register,user_login,user_logout
from django.urls import path

urlpatterns = [
   path('',post_list,name='home'),
   path('register/',register,name='register'),
   path('login/',user_login,name='login'),
   path('logout/',user_logout,name='logout'),
   path('profile/',profile,name='profile'),
   
  
]
