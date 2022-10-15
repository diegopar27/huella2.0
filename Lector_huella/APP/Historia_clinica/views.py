from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from .models import historia
from .serializers import HistoriaSerializer


class HistoriaListAPIView(APIView):

    def get(self, request,):
        historias = HistoriaSerializer(historia.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data=historias.data)