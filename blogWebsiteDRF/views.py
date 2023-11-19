from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from django.shortcuts import render, HttpResponse

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