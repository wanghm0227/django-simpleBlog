from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<int:pk>/settings/', views.ChangeSettingView.as_view(), name='settings'),
    path('password/', views.ChangePassword.as_view(), name='change_password'),
]
