from .serializers import CustomUserSerializer, CreateCustomUserSerializer, UserDeleteOrUpdateSerializer, CreateGroupSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import search_users, CustomUser
from django.contrib.auth.models import Group
from .permissions import IsManager, IsSupervisor
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status

User = get_user_model()


class CustomUserSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q", '')
        users = search_users(query) if query else User.objects.none()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    




class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateCustomUserSerializer
    




class DeleteOrEditUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, slug):
        return get_object_or_404(CustomUser, slug=slug)
    


    def put(self, request, slug):
        user = self.get_object(slug)
        serializer = UserDeleteOrUpdateSerializer(user, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def patch(self, request, slug):        
        user = self.get_object(slug)
        serializer = UserDeleteOrUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    def delete(self, request, slug):
        user = self.get_object(slug)
        user.delete()
        return Response({"detail":"user deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
    



class CreateGroupView(APIView):
    permission_classes = [IsAuthenticated, IsManager]


    def post(self, request):
        serializer = CreateGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"The Group Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




 