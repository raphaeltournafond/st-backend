from django.urls import path
from .views import SessionCreate, SessionDetail, SessionList

urlpatterns = [
    path('sessions/', SessionCreate.as_view(), name='session_create'),
    path('sessions/list/<int:user_id>/', SessionList.as_view(), name='session_list'),
    path('sessions/<int:session_id>/', SessionDetail.as_view(), name='session_detail'),
]
