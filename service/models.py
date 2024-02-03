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


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='тема письма')
    message = models.TextField(verbose_name='тело письма')
    user_for = models.ForeignKey(Сustomer, on_delete=models.CASCADE,
                                 verbose_name='получатель сообщения', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Letter(models.Model):
    day = "раз в день"
    week = "раз в неделю"
    month = "раз в месяц"

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    choice_periodicity = [(day, "раз в день"), (week, "раз в неделю"), (month, "раз в месяц")]
    choice_status = [(CREATED, "создана"), (STARTED, "запущена"), (COMPLETED, "завершена")]
    time_on = models.TimeField(verbose_name='время рассылки от')
    time_off = models.TimeField(verbose_name='время рассылки до')
    time = models.TimeField(verbose_name='Время рассылки', **NULLABLE)
    finish_date = models.DateField(verbose_name='Дата завершения рассылки', default='2024-01-01')
    finish_time = models.TimeField(verbose_name='Время завершения рассылки', default='00:00')
    periodicity = models.CharField(max_length=100, verbose_name='переодичность рассылки',
                                   choices=choice_periodicity)
    status = models.CharField(max_length=100, verbose_name='статус рассылки', choices=choice_status)
    clients = models.ManyToManyField(Сustomer, verbose_name='клиенты рассылки')
    name = models.CharField(max_length=100, verbose_name='название рассылки', **NULLABLE)
    is_active = models.BooleanField(verbose_name='активность рассылки', default=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Автор',
                               **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение',
                                **NULLABLE)
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return self.time_on, self.time_off

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

        permissions = [
            ('can_change_is_active_permission', 'Can change active latter'),
        ]


class Logs(models.Model):
    data_time = models.DateTimeField(verbose_name='Дата и время отправки', **NULLABLE)
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
