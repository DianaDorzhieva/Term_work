from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}
AUTH_USER_MODEL = 'users.User'

class User(AbstractUser, models.Model):
    DoesNotExist = None
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    FIO = models.CharField(max_length=300, verbose_name='ФИО',  **NULLABLE)
    comment = models.TextField(verbose_name='комментарий',  **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон')
    county = models.CharField(max_length=50, verbose_name='страна')
    email_verification_token = models.CharField(max_length=255, **NULLABLE)
    is_bloked = models.BooleanField(verbose_name='блокировка пользователя', default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            ('can_change_is_bloked_permission', 'Can bloked user'),
        ]
