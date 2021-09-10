from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('password/', views.ChangePassword.as_view(), name='change_password'),
]
