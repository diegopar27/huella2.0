from django.shortcuts import render

# Create your views here.
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserListAPIView(APIView):

    def get(self, request,):
        Users= UserSerializer(User.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=Users.data)