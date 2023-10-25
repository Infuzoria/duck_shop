from django.urls import path
from catalog.views import ProductListView, RequestCreateView, ProductDetailView, PostCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    #path('product/', product),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
