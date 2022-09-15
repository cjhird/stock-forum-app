from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from django.conf import settings
import jwt

# Serializer
from .serializers.common import UserSerializer

# Model
from django.contrib.auth import get_user_model
User = get_user_model()

# create your views here

# Register
class RegisterView(APIView):

  def post(self, request):
    user_to_add = UserSerializer(data=request.data)
    print('request register--->', request.data)

    try:
        user_to_add.is_valid(True)
        print(user_to_add.errors)
        user_to_add.save()
        return Response({ 'message': 'Registration Successful' }, status.HTTP_202_ACCEPTED)
    except ValidationError:
        return Response(user_to_add.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        print(e)
        return Response({ 'detail': str(e) }, status.HTTP_422_UNPROCESSABLE_ENTITY)

# Login
class LoginView(APIView):

  def post(self, request):
      email = request.data.get('email')
      password = request.data.get('password')

      try:
        user_to_validate = User.objects.get(email=email)
      except User.DoesNotExist:
          raise PermissionDenied('Invalid credentials')

      if not user_to_validate.check_password(password):
        raise PermissionDenied('Invalid credentials')

      dt = datetime.now() + timedelta(hours=3)

      token = jwt.encode(
        {
            'sub': user_to_validate.id,
            'exp': int(dt.strftime('%s'))
        },
        settings.SECRET_KEY,
        algorithm='HS256'
      )

      return Response({ 'message': f"Welcome back, {user_to_validate.username}", 'token': token }, status.HTTP_202_ACCEPTED)