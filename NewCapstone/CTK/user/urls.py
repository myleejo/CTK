from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

app_name = 'user'

urlpatterns = [
    path('join/', Join.as_view(), name='join'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('reset_password/', ResetPassword.as_view(), name='reset_password'),
    #path('reset_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

