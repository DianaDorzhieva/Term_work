from django import forms

from blog.models import Blog
from service.forms import StyleFormMixin

class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text',  'image', 'is_published')


