from users.views import home, register,user_login,user_logout
from django.urls import path

urlpatterns = [
   path('',home,name='home'),
   path('register/',register,name='register'),
   path('login/',user_login,name='login'),
   path('logout/',user_logout,name='logout'),
  
   
  
]
