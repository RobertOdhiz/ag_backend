from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import NewUser
from .serializers import CustomLoginSerializer, UserSerializer, UserIDSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
import json

NewUser = get_user_model()

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        """
        Perform the creation of a User instance.

        Hashes the password before saving the user.

        Parameters:
        - serializer: UserSerializer instance.
        """
        # Hash the password before saving the user
        serializer.save(password=make_password(serializer.validated_data['password']))

class CustomTokenObtainPairView(APIView):
    """Custom view to obtain an access token and refresh token"""
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        user_data = {
            'user_id': str(user.id),
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        json_data = json.dumps(user_data)
        response = Response(status=status.HTTP_200_OK)
        response.set_cookie(
            key='auth_cookie',
            value=json_data,
            secure=False,
            max_age=60 * 60 * 24 * 7,  # 7 days
            httponly=True
        )

        return response


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserIDSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user
    

class GetUserDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user  # Get the authenticated user
        user_data = {'id': user.id}  # Create a dictionary with only the 'id' field
        return Response(user_data, status=status.HTTP_200_OK)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
