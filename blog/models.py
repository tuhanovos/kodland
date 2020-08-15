from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.urls import reverse
from filer.utils.files import slugify


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Статья", unique=True)
    slug = models.SlugField(max_length=200, verbose_name="Слаг", unique=True)
    content = RichTextField(config_name='default', verbose_name='Текст статьи', max_length=3000)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    image = models.ImageField(verbose_name='Изображение статьи', upload_to='uploads/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'