from .views import RegisterAPI, LoginAPI, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('changepassword', ChangePasswordView.as_view(), name="ChangePasswordView")
]