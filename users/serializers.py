from rest_framework import serializers
from .models import CustomUser 

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in response, but allow it in requests
    date_joined = serializers.DateTimeField(read_only=True)  # Read-only field, won't be sent in the POST request
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 
                  'is_active', 'profile_picture', 'role', 'phone_number', 'password', 'date_joined']  # Include all fields

from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password', 'profile_picture', 'role', 'first_name', 'last_name', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be returned in responses
        }

    def create(self, validated_data):
        """
        Create and return a new user instance with hashed password.
        """
        # Ensure is_staff and is_superuser are set if they are provided
        is_staff = validated_data.get('is_staff', False)  # Default to False if not provided
        is_superuser = validated_data.get('is_superuser', False)  # Default to False if not provided

        # Creating the user with the provided fields
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            profile_picture=validated_data.get('profile_picture'),
            role=validated_data.get('role', 'user'),  # default to 'user' if no role is provided
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        return user
