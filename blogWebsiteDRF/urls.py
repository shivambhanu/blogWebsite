from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('api/list', views.ListBlogView.as_view(), name='ListBlogView'),
    path('api/create', views.CreateBlogView.as_view(), name='CreateBlogView'),
    path('api/destroy/<int:pk>', views.DestroyBlogView.as_view(), name='DestroyBlogView'),
    path('retreive_blog', views.get_blog_view, name='get_blog_view'),
]
