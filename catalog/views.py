from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, email, message)
    return render(request, 'contacts.html')


def product(request, pk):
    context = {
        "object_name": Product.objects.filter(id=pk)[0].__dict__['name'],
        "object_description": Product.objects.filter(id=pk)[0].__dict__['description'],
        "object_image": Product.objects.filter(id=pk)[0].__dict__['image']
    }
    #print(context['object_list'][0].__dict__['name'])
    return render(request, 'product.html', context)
