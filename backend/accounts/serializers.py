from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    # username is auto-set from email — not required from the frontend
    username = serializers.CharField(required=False, default="")
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    role = serializers.ChoiceField(choices=["admin", "client"], write_only=True, required=False, default="client")

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password", "password2", "role")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        validated_data.pop("username", None)  # remove username — we set it from email below
        email = validated_data["email"]
        role = validated_data.pop("role", "client")
        is_staff = True if role == "admin" else False
        user = User.objects.create_user(
            username=email,   # use email as username (unique)
            email=email,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            password=validated_data["password"],
            is_staff=is_staff
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "role")

    def get_role(self, obj):
        return "admin" if obj.is_staff else "client"
