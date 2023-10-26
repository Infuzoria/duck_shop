from django.shortcuts import render
from catalog.models import Product, Request, Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'


class RequestCreateView(CreateView):
    model = Request
    template_name = 'contacts.html'
    fields = ('name', 'email', 'message')
    success_url = '/contacts'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_name'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['name']
        context_data['object_description'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['description']
        context_data['object_image'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['image']

        return context_data


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'text', 'image', 'date')
    success_url = '/posts'


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_title'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['title']
        context_data['object_text'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['text']
        context_data['object_image'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['image']

        return context_data


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'text', 'image', 'date')
    success_url = '/posts'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/posts'
