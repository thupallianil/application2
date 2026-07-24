from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import secrets

from .serializers import RegisterSerializer, UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/auth/register/
    Body: { email, password, password2, first_name, last_name }
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = secrets.token_hex(32)
        return Response(
            {
                "success": True,
                "message": "Account created successfully.",
                "token": token,
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/auth/login/
    Body: { email, password }
    """
    email = request.data.get("email", "").strip()
    password = request.data.get("password", "")

    if not email or not password:
        return Response(
            {"error": "Email and password are required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Django uses username for auth; we set username = email on register
    user = authenticate(request, username=email, password=password)

    if user is None:
        # Try fetching by email in case username differs
        try:
            db_user = User.objects.get(email=email)
            user = authenticate(request, username=db_user.username, password=password)
        except User.DoesNotExist:
            pass

    if user is None:
        return Response(
            {"error": "Invalid email or password."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    if not user.is_active:
        return Response(
            {"error": "Account is disabled."},
            status=status.HTTP_403_FORBIDDEN,
        )

    token = secrets.token_hex(32)
    return Response(
        {
            "success": True,
            "message": "Login successful.",
            "token": token,
            "user": UserSerializer(user).data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def me_view(request):
    """GET /api/auth/me/ — returns current user info (stub)"""
    return Response({"detail": "Auth not fully implemented."}, status=200)
