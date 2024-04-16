from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from .permissions import IsAdminOrSelf
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

class Register(APIView):
    """
    View to register a new user in the system.
    """

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Registration successful', 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Login(TokenObtainPairView):
    """
    Log a user from the system.
    """

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = super(Login, self).post(request, *args, **kwargs)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserDetail(APIView):
    """
    Manage user details from the system.

    * Requires token authentication.
    * Only admin or actual users are able to access this view.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSelf]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(self.request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)