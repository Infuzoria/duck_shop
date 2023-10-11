from django.urls import path
from catalog.views import home_page, contacts, product

app_name = 'catalog'

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts),
    #path('product/', product),
    path('product/<int:pk>/', product, name='product'),
]
