from django.shortcuts import render
from catalog.models import Product


def home_page(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'home_page.html', context)


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, email, message)
    return render(request, 'contacts.html')


def product_page(request):
    return render(request, 'product.html')
