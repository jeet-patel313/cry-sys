from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('access/', views.accessPage, name="accessPage"),
   path('blogs/', views.blogs, name="blogs"),
   path('about/', views.about, name="about"),
   path('register/', views.registerPage, name="register"),
   path('login/', views.loginPage, name="login"),
   path('logout/', views.logoutUser, name="logout"),
   path('prices/', views.prices, name="prices"),
   
]
