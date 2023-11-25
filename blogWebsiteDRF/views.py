from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from django.shortcuts import render, HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.
class ListBlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlogView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class DestroyBlogView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UpdateBlogView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    
def home_view(request):
    return render(request, 'home.html')

def get_blog_view(request):
    author = request.GET.get('author')
    blog = Blog.objects.get(author=author)
    return render(request, 'result.html', {'blog': blog})

def single_blog_view(request, author=None):
    blog = Blog.objects.get(author=author)
    return render(request, 'result.html', {'blog': blog})

def list_blogs_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        managers.user_set.add(user)
        return Response({"message": "ok"})
    return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)