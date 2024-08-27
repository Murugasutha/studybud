from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginpage, name="login"),
    path('register', views.registeruser, name="register"),
    path('logout',views.logoutuser,name="logout"),
    path('user-profile/<str:pk>/',views.userprofile,name="user-profile"),
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room',views.createRoom, name="create-room"),
    path('update-room/<str:pk>/',views.updateroom, name="update-room"),
    path('delete-room/<str:pk>/',views.deleteroom, name="delete-room"),
    path('delete-message/<str:pk>/',views.deletemessage, name="delete-message"),
    path('update-user/<str:pk>/',views.updateUser, name="update-user"),

]