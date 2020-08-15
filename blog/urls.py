from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from blog.views import ArticleListView, ArticleDetailView, ArticleAddView

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('blog/article/add/', ArticleAddView.as_view(), name='article-add'),
    path('blog/article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('blog/article/create/', ArticleAddView.as_view(), name='article-create')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)