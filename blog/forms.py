from ckeditor.widgets import CKEditorWidget
from django import forms

from blog.models import Article


class AddArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
