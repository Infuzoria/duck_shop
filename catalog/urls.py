from django.urls import path
from catalog.views import (ProductListView, RequestCreateView, ProductDetailView, PostCreateView, PostListView,
                           PostDetailView)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name="list_of_posts"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
]
