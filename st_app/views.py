from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Session
from .serializers import SessionSerializer
from .permissions import IsAdminOrSelf
from rest_framework_simplejwt.authentication import JWTAuthentication

class SessionList(APIView):
    """
    View to list all sessions.
    """
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        sessions = Session.objects.filter(user=user)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)
    
class SessionCreate(APIView):
    """
    View to create a new session.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSelf]
    
    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.data[Session.user.field.name]
            user = get_object_or_404(User, id=user_id)
            self.check_object_permissions(request, user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetail(APIView):
    """
    View to retrieve and delete a session.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSelf]

    def get(self, request, session_id):
        session = get_object_or_404(Session, id=session_id)
        self.check_object_permissions(request, session.user)
        serializer = SessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, session_id):
        session = get_object_or_404(Session, id=session_id)
        self.check_object_permissions(request, session.user)
        session.delete()
        return Response(data={"message": "Session deleted successfully"}, status=status.HTTP_204_NO_CONTENT)