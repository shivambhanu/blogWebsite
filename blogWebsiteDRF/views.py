from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from django.shortcuts import render

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


    
    
def home_view(request):
    return render(request, 'home.html')

def get_blog_view(request):
    pk = request.GET.get('id')
    blog = Blog.objects.get(pk=pk)
    return render(request, 'result.html', {'blog': blog})
