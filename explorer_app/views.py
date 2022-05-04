from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins
from rest_framework import generics
from explorer_app.models import Post
from explorer_app.serializers import PostSerializer, CreatePostSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import requests
from .helpers import *


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, krisskad'}
        return Response(content)


class PostDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImagesView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, page):
        all_data = get_imgur_images(page=page)

        # queryset = {
        #     "data":all_data
        # }
        # print(page, 11111111111111111)
        # return all_data
        # content = {'message': 'Hello, krisskad'}
        return Response(all_data)


class ImageList(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        page = self.kwargs['page']

        all_data = get_imgur_images(page=page)

        # queryset = {
        #     "data":all_data
        # }
        print(page, 11111111111111111)
        return all_data