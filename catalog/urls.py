from django.urls import path
from catalog.views import (ProductListView, RequestCreateView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, VersionCreateView, VersionListView, VersionDeleteView, VersionUpdateView,
                           toggle_activity)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('versions/', VersionListView.as_view(), name='versions'),
    path('delete_version/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),
    path('update_version/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
]
