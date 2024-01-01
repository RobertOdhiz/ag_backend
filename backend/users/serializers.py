# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers

NewUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = NewUser
        fields = ("first_name", 'last_name', 'email', 'address', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

class UserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("id",)

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = NewUser.objects.filter(email=email).first()

            if user:
                if not user.check_password(password):
                    raise serializers.ValidationError('Incorrect password')
            else:
                raise serializers.ValidationError('User with this email does not exist')

            attrs['user'] = user
            return attrs
        else:
            raise serializers.ValidationError('Both email and password are required')
