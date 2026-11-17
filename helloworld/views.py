from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Post
from .serializers import PostSerializer
from .permissions import IsPostPossessor


# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "hello world"})


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
