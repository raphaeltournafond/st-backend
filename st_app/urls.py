from django.urls import path
from .views import SessionCreate, SessionDetail

urlpatterns = [
    path('sessions/', SessionCreate.as_view(), name='session_create'),
    path('sessions/<int:session_id>/', SessionDetail.as_view(), name='session_detail'),
]
