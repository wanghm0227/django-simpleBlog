from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<int:pk>/settings/', views.ChangeSettingView.as_view(), name='settings'),
    path('password/', views.ChangePassword.as_view(), name='change_password'),
    path('<int:pk>/profile/', views.ShowProfileView.as_view(), name='profile'),
    path('<int:pk>/edit_profile/',
         views.EditProfileView.as_view(), name='edit_profile'),
    path('create_profile/',
    views.CreateProfileView.as_view(), name='create_profile'),

]
