from django.urls import path
from users.views import LoginView, RegisterView, verify_email, logout_view

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/email',verify_email, name='code'),
    path('logout/', logout_view,name='logout'),
]