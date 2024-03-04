from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import NewUser
import json

class CustomCookieAuthentication(JWTAuthentication):
    """
    Custom authentication class using cookies for user ID and access token stored in JSON format.
    """

    def authenticate(self, request):
        """
        Overrides the default authenticate method to use cookies.
        """
        auth_cookie = request.COOKIES.get('auth_cookie')
        if not auth_cookie:
            return None

        # Try to decode the JSON cookie
        try:
            data = json.loads(auth_cookie)
            user_id = data['user_id']
            access_token = data['access_token']
        except (json.JSONDecodeError, KeyError):
            raise AuthenticationFailed('Invalid cookie format')

        # Validate user and access token
        try:
            user = self.get_user(user_id)
            if not user or not self.validate_token(user, access_token):
                raise AuthenticationFailed('Invalid user or access token')
        except Exception as e:
            raise AuthenticationFailed('Invalid access token: {}'.format(e))

        return (user, access_token)

    def get_user(self, user_id):
        """
        Retrieves the user object based on the extracted user ID.
        """
        try:
            return NewUser.objects.get(pk=user_id)
        except NewUser.DoesNotExist:
            return None

    def validate_token(self, user, access_token):
        """
        Validates the access token associated with the user.
        """
        from rest_framework_simplejwt.tokens import Token

        try:
            # Use the access_token to create a Token object
            token = Token(access_token)
            # Check if the token is valid and belongs to the provided user
            if token.user == user and token.is_valid:
                return True
            else:
                return False
        except Exception:
            return False
