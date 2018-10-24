from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LoginUser
from .serializers import UserSerializer

class login(APIView):

    def get(self, request):
        Users = LoginUser.objects.all()
        serializer = UserSerializer(Users, many=True)

        return Response(serializer.data)


        print(serializer.data)