import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from service.models import Logs, Letter
from datetime import datetime


class MessageService:

    def __init__(self, mailing):
        self.mailing = mailing

    def create_task(self):
       pass

    def crontab_create(self):

       pass

    def finish_task(mailing):

       pass

    def delete_task(mailing):

       pass

    def send_mailing(mailing):
        """Отправка рассылки и создание лога рассылки"""
        pass

def get_count_mailing():
        pass

def get_active_mailing():
        pass

def get_unique_clients():
        pass
