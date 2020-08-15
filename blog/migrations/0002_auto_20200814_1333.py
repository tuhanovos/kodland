# Generated by Django 3.1 on 2020-08-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d', verbose_name='Изображение статьи'),
        ),
    ]