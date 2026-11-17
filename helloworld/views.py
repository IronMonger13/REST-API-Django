from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer


# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "hello world"})


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
