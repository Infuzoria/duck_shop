from django.urls import path
from catalog.views import ProductListView, contacts, product

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home_page'),
    path('contacts/', contacts),
    #path('product/', product),
    path('product/<int:pk>/', product, name='product'),
]
