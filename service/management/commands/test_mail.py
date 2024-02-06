from django.core.management import BaseCommand
from service.service import send_mailing
from service.models import Letter
class Command(BaseCommand):

    def handle(self, *args, **options):
        letter = Letter.objects.last()
        send_mailing(letter)
