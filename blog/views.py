from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from config import settings
from django.core.cache import cache


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
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

        if settings.CACHE_ENABLED:
            text_key = f'post_text_{self.object.pk}'
            photo_key = f'post_photo_{self.object.pk}'
            post_text = cache.get(text_key)
            post_photo = cache.get(photo_key)

            if post_text is None:
                post_text = Post.objects.filter(id=self.object.pk)[0].__dict__['text']
                cache.set(text_key, post_text)
            elif post_photo is None:
                post_photo = Post.objects.filter(id=self.object.pk)[0].__dict__['image']
                cache.set(photo_key, post_photo)

        else:
            post_text = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['text']
            post_photo = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['image']

        context_data['object_title'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['title']
        context_data['object_text'] = post_text
        context_data['object_image'] = post_photo
        context_data['views_count'] = Post.objects.filter(id=self.kwargs.get('pk'))[0].__dict__['views_count']

        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
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
        return reverse('blog:post_view', args=[self.kwargs.get('pk')])


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    success_url = '/posts'
