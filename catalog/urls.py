from django.urls import path
from catalog.views import (ProductListView, RequestCreateView, ProductDetailView, PostCreateView, PostListView,
                           PostDetailView, PostUpdateView, PostDeleteView)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name="list_of_posts"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='post_view'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
