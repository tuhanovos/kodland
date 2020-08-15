from django.contrib import admin

# Register your models here.
from blog.models import Article


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'image']
    prepopulated_fields = {'slug': ('title',)}
