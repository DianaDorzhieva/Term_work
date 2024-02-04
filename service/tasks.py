from celery import shared_task
from service.models import Letter
from service.service import finish_task, delete_task, send_mailing


@shared_task(name='send_message')
def send_message(mailing_id):
    mailing = Letter.objects.get(pk=mailing_id)
    if finish_task(mailing):
        delete_task(mailing)
        return
    return send_mailing(mailing)
