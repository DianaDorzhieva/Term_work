from random import sample
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView

from blog.models import Blog

from service.models import Сustomer, Letter, Message, Logs
from django.urls import reverse_lazy, reverse

from service.forms import СustomerForm, LetterForm, MessageForm
from django.forms import inlineformset_factory

from service.service import MessageService, get_count_mailing, get_active_mailing, \
    get_unique_clients


class СustomerListView(LoginRequiredMixin, ListView):
    model = Сustomer

    def get_queryset(self):
        customer_list = super().get_queryset()
        if self.request.user.is_bloked == True:
            raise Http404("Вы заблокрованы")
        else:
            return customer_list


class СustomerCreateView(LoginRequiredMixin, CreateView):
    model = Сustomer
    form_class = СustomerForm
    success_url = reverse_lazy('service:list')




class СustomerDetailView(LoginRequiredMixin, DetailView):
    model = Сustomer


class СustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Сustomer
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('service:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не можете редактировать чужого пользователя")
        return self.object


class СustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Сustomer
    success_url = reverse_lazy('service:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не можете удалять другого пользователя")
        return self.object


class LetterListView(LoginRequiredMixin, ListView):
    model = Letter

    def get_queryset(self):
        letter_list = super().get_queryset()
        if self.request.user.is_bloked == True:
            raise Http404("Вы заблокрованы")
        else:
            return letter_list


class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('service:list_letter')

    def form_valid(self, form):
        mail = form.save(commit=False)
        mail.author = self.request.user
        mail.status = 'CREATED'
        mail.save()

        message_service = MessageService(mail)
        message_service.send_mailing(mail)
        message_service.create_task()
        mail.status = 'STARTED'
        mail.save()

        return super(LetterCreateView, self).form_valid(form)


class LetterDetailView(LoginRequiredMixin, DetailView):
    model = Letter


class LetterUpdateView(LoginRequiredMixin, UpdateView):
    model = Letter
    form_class = LetterForm
    success_url = reverse_lazy('service:list_letter')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MessageFormset = inlineformset_factory(Letter, Message, extra=1, form=MessageForm)

        if self.request.method == 'POST':
            context_data['formset'] = MessageFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = MessageFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не можете редактировать чужую подписку")
        return self.object


class LetterDeleteView(LoginRequiredMixin, DeleteView):
    model = Letter
    success_url = reverse_lazy('service:list_letter')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не можете удалить чужую подписку")
        return self.object





class HomeView(TemplateView):
    """Представление главной страницы сервиса"""
    extra_context = {
        'title': 'SkyBlog'
    }
    template_name = 'service/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(Blog.objects.all())
        context['random_post'] = sample(all_posts, min(3, len(all_posts)))
        context['count_mailing'] = get_count_mailing()
        context['active_mailing'] = get_active_mailing()
        context['unique_clients'] = get_unique_clients()

        return context




def toggle_status(request, pk):
    """Функция, позволяющая отключать и активировать рассылку"""
    mailing = get_object_or_404(Letter, pk=pk)
    message_service = MessageService(mailing)
    if mailing.status == 'STARTED' or mailing.status == 'CREATED':
        message_service.delete_task(mailing)
        mailing.status = 'COMPLETED'
    else:
        message_service.create_task()
        mailing.status = 'STARTED'

    mailing.save()

    return redirect(reverse('service:list_letter'))
