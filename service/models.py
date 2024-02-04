from django.db import models

AUTH_USER_MODEL = 'users.User'
NULLABLE = {'blank': True, 'null': True}


class Сustomer(models.Model):
    email = models.EmailField(verbose_name='почта')
    name = models.CharField(max_length=300, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий')
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор',
                               **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Letter(models.Model):

    choice_periodicity = [('day', "раз в день"), ('week', "раз в неделю"), ('month', "раз в месяц")]
    choice_status = [('CREATED', "создана"), ('STARTED', "запущена"), ('COMPLETED', "завершена")]

    time = models.TimeField(verbose_name='Время рассылки', **NULLABLE, auto_now_add=True,)
    finish_date = models.DateField(verbose_name='Дата завершения рассылки', **NULLABLE)
    finish_time = models.TimeField(verbose_name='Время завершения рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=100, verbose_name='переодичность рассылки',
                                   choices=choice_periodicity)
    status = models.CharField(max_length=100, verbose_name='статус рассылки', choices=choice_status)
    clients = models.ManyToManyField(Сustomer, verbose_name='клиенты рассылки')
    name = models.CharField(max_length=100, verbose_name='название рассылки', **NULLABLE)
    is_active = models.BooleanField(verbose_name='активность рассылки', default=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор',
                               **NULLABLE)
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

        permissions = [
            ('can_change_is_active_permission', 'Can change active latter'),
        ]

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.status = 'COMPLETED'
        self.save()


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма', **NULLABLE)
    message = models.ForeignKey(Letter, on_delete=models.CASCADE,
                                verbose_name='настройка сообщения', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.CharField(max_length=100, verbose_name='статус попытки')
    answer = models.BooleanField(verbose_name='ответ почтового сервера')

    mailing_list = models.ForeignKey(Letter, on_delete=models.CASCADE,
                                     verbose_name='рассылка', **NULLABLE)
    client = models.ForeignKey(Сustomer, on_delete=models.CASCADE, verbose_name='клиент рассылки',
                               **NULLABLE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'логи'
        verbose_name_plural = 'логи'
