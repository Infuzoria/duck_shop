from django.urls import path
from catalog.views import (ProductListView, RequestCreateView, ProductDetailView, PostCreateView, PostListView,
                           PostDetailView, PostUpdateView, PostDeleteView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, VersionCreateView, VersionListView, VersionDeleteView)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('posts/', PostListView.as_view(), name="list_of_posts"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='post_view'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('versions/', VersionListView.as_view(), name='versions'),
    path('delete_version/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),
]
