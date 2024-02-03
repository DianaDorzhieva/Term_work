from blog.apps import BlogConfig
from django.urls import path

from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogConfig.name
urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='blog_update')

]
