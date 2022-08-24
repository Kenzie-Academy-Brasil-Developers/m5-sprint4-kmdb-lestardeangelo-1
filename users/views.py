from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination

from .models import User
from .permissions import IsUserOwnerOrAdmin
from .serializers import LoginSerializer, UserSerializer


class UserView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        result_page = self.paginate_queryset(users, request, view=self)
        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUserOwnerOrAdmin]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key})
        
        return Response(
              {"detail": "invalid username or password"},
              status=status.HTTP_400_BAD_REQUEST,
        )
