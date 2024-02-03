from django.contrib import admin

from service.models import Сustomer, Letter, Message, Logs


@admin.register(Сustomer)
class СustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment',)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('periodicity', 'status', )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'user_for',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('status', 'answer',)



