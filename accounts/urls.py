from django.urls import path
from .views import Register, Login, UserList

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('users/', UserList.as_view(), name='list_users'),
]