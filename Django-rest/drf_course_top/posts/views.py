from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer, UserSerializer
from .models import Post

from rest_framework import generics
from rest_framework import  mixins
from rest_framework import permissions
from .permissions import IsOwner

from django.contrib.auth.models import User


# @csrf_exempt
# def post_view(request):
#     # GET
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many = True)
    # return JsonResponse(data=serializer.data, safe=False) 

# dict/ ->  OrderedDict

# class PostView(APIView):

#     def get(self, request, *args, **kwargs): 
#         if 'pk' in kwargs:
#             post = Post.objects.get(id=kwargs['pk'])
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         else:
#             queryset = Post.objects.all()
#             serializer = PostSerializer(queryset, many = True)
#             return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id=pk)
#         post.delete()
#         return Reponse()

    
# # put=update
#     def put(self, request, pk, *args, **kwargs):
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


class PostListView(mixins.ListModelMixin,
mixins.CreateModelMixin,
 generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class PostDetailView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)


# permissions.IsAuthenticated - if user is logged in
# permissions.IsAdminUser - if user is staff user
# permissions.AllowAny - everyone can access
# permissions.IsAuthenticatedOrReadOnly - if not logged in then can only read


    
class UserDetailView(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

