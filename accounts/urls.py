from django.urls import path
from .views import Register, Login, UserList, UserDetail, TokenDecode

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:user_id>/', UserDetail.as_view(), name='user_detail'),
    path('users/decode/', TokenDecode.as_view(), name='token_decode'),
]