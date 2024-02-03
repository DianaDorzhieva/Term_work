from celery import shared_task
from service.models import Letter
from service.service import MessageService


@shared_task(name='send_message')
def send_message(mailing_id):
    mailing = Letter.objects.get(pk=mailing_id)
    if MessageService.finish_task(mailing):
        MessageService.delete_task(mailing)
        return
    return MessageService.send_mailing(mailing)
