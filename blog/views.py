from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView

from blog.forms import AddArticleForm
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    paginate_by = 10


class ArticleAddView(CreateView):
    model = Article
    template_name = 'blog/form_add_article.html'
    form_class = AddArticleForm
    success_url = reverse_lazy('blog:article-list')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'
    slug_url_kwarg = 'slug'
