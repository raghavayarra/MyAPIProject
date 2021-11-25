from django import http
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])

def showall(request):
    post=Post.objects.all()

    url=request.query_params['url']
    if url != None:
        post = Post.objects.get(url=url)
        serializer=PostSerializer(post)
        return Response({'message':" This is malware url"})

    else:
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data)


@api_view(['POST'])

def create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
