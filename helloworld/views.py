from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Post
from .serializers import PostSerializer
from .permissions import IsPostPossessor
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "hello world"})


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = PostFilter
    search_fields = ["title", "content"]
    ordering_fields = ["id"]

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
