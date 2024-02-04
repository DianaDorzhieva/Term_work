from django.core.management import BaseCommand
from blog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        blog_list = [
            {'title': 'ручки', 'text': 'хорошо пишет'}

        ]
        blog_objects = []

        for item in blog_list:
            blog_objects.append(Blog(**item))
        Blog.objects.bulk_create(blog_objects)
