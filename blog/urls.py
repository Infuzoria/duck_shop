from django.urls import path
from blog.views import PostCreateView, PostUpdateView, PostDetailView, PostListView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name="list_of_posts"),
    path('view/<int:pk>/', PostDetailView.as_view(), name='post_view'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
