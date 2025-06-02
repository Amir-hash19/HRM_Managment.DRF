from rest_framework.views import APIView
from rest_framework.response import Response
from .models import search_users
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer



User = get_user_model()


class CustomUserSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q", '')
        users = search_users(query) if query else User.objects.none()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    