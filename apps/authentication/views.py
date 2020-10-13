from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    # we allow all the users to access this view
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AutoLoginView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LoginSerializer

    def get(self, request):
        print(request)
        user = {
            "username": request.user.username,
            "user_id": request.user.id,
            "email": request.user.email,
            "collection_id": request.user.collection.id
        }

        serializer = self.serializer_class(data=user)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
