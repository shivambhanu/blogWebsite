from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_view, name='home_view'),
    path('', views.list_blogs_view, name='list_blogs_view'),
    path('api/list', views.ListBlogView.as_view(), name='ListBlogView'),
    path('api/create', views.CreateBlogView.as_view(), name='CreateBlogView'),
    path('api/destroy/<str:pk>', views.DestroyBlogView.as_view(), name='DestroyBlogView'),
    path('api/update/<str:pk>', views.UpdateBlogView.as_view(), name='UpdateBlogView'),
    path('retreive-blog', views.get_blog_view, name='get_blog_view'),
    path('single-blog/<str:author>', views.single_blog_view, name='single_blog_view'),
]
