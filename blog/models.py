from django.db import models
from django.urls import reverse

NULLABLE = {'blank': True, 'null': True}
AUTH_USER_MODEL = 'users.User'

class Blog(models.Model):
    activity = [(True, 'Опубликовано'),
                (False, 'Неопубликовано')]

    title = models.CharField(max_length=100, verbose_name='название')
    slug = models.SlugField(max_length=255, unique=True, **NULLABLE, verbose_name='URL')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор', **NULLABLE)
    text = models.TextField(verbose_name='текст', **NULLABLE)
    image = models.ImageField(upload_to='blogs/', verbose_name='изображение', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(verbose_name='признак публикации', default=True, choices=activity)
    count_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})


