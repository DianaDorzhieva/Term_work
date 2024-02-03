from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.utils import timezone
from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        product_list = super().get_queryset()
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser and self.request.user.is_bloked == False:
            return product_list
        elif self.request.user.is_bloked == True:
            raise Http404("Вы заблокрованы")
        else:
            return product_list.filter(is_published=True)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.date_create = timezone.localtime(timezone.now())
        self.object.save()
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не можете удалять чужую статью")
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не являетесь автором данной статьи")
        return self.object
