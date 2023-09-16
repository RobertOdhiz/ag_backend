from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import NewUser
from .serializers import CustomLoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

NewUser = get_user_model()

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(APIView):
    """Custom view to obtain an access token and refresh token"""
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        response = Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
        response['Authorization'] = f'Bearer {refresh.access_token}'

        return response


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = NewUser.objects.all()
        usernames = [user.email for user in users]
        return Response(usernames)
