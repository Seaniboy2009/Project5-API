from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.http import Http404


class PostList(APIView):
    '''
    Get all posts and list them
    '''
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={ 'request': request })
        return Response(serializer.data)


class PostDetail(APIView):
    '''
    Get one post by primary key and return
    '''
    
    # change the serializer class to be a form for input
    serializer_class = PostSerializer

    def get_post(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        post = self.get_post(pk)
        serializer = PostSerializer(post, context={ 'request': request })
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = self.get_post(pk)
        serializer = PostSerializer(post, data=request.data, context={ 'request': request })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
