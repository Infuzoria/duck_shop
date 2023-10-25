from django.urls import path
from catalog.views import ProductListView, RequestCreateView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', RequestCreateView.as_view()),
    #path('product/', product),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
