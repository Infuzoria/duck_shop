from django.shortcuts import get_object_or_404, redirect

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Request, Version
from mailing_app.models import Newsletter, Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_product'
    model = Product
    form_class = ProductForm
    success_url = '/'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.change_product'
    model = Product
    form_class = ProductForm
    success_url = '/'


class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'
    queryset = Product.objects.order_by('?')[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.groups.filter(name='manager').exists():
            context['total_mailings'] = Newsletter.objects.all().count()
            context['active_mailings'] = Newsletter.objects.filter(is_active=True).count()
            context['total_clients'] = Client.objects.all().distinct('email').count()
        elif user.groups.filter(name='user').exists():
            context['total_mailings'] = Newsletter.objects.filter(owner=user).count()
            context['active_mailings'] = Newsletter.objects.filter(owner=user, is_active=True).count()
            context['total_clients'] = Client.objects.filter(owner_id=user.id).count()
        return context


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
        versions = Version.objects.filter(product=self.kwargs.get('pk'), is_active=True)
        if len(versions) > 0:
            active_version = versions[len(versions)-1]
            print(versions)
        else:
            active_version = None

        context_data = super().get_context_data(**kwargs)
        context_data['object_name'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['name']
        context_data['object_description'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['description']
        context_data['object_image'] = Product.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['image']
        if active_version:
            self.object.active_version = str(active_version)
            self.object.save()
            context_data['active_version'] = active_version

        return context_data


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_product'
    model = Product
    success_url = '/'


"""class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_post'
    model = Post
    fields = ('title', 'text', 'image', 'date')
    success_url = '/posts'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class PostListView(ListView):
    model = Post

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        queryset = queryset.order_by('?')[:3]
        return queryset


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
        context_data['views_count'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['views_count']

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.change_post'
    model = Post
    fields = ('title', 'text', 'image', 'date')
    success_url = '/posts'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:post_view', args=[self.kwargs.get('pk')])


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_post'
    model = Post
    success_url = '/posts'"""


class VersionCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.add_version'
    model = Version
    form_class = VersionForm
    success_url = '/versions'


class VersionUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.change_version'
    model = Version
    form_class = VersionForm
    success_url = '/versions'


class VersionListView(PermissionRequiredMixin, ListView):
    permission_required = 'catalog.view_version'
    model = Version


class VersionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_version'
    model = Version
    success_url = '/versions'


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.groups.filter(name='manager').exists():
            context['total_mailings'] = Newsletter.objects.all().count()
        else:
            context['total_mailings'] = Newsletter.objects.filter(user=user).count()

        return context


def toggle_activity(request, pk):
    version_item = get_object_or_404(Version, pk=pk)
    if version_item.is_active:
        version_item.is_active = False
    else:
        version_item.is_active = True

    version_item.save()
    return redirect(reverse('catalog:versions'))
