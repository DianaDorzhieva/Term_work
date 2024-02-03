from django.urls import path
from service.apps import ServiceConfig
from service.views import СustomerListView, СustomerCreateView, СustomerDetailView, \
    СustomerUpdateView, СustomerDeleteView, LetterListView, LetterCreateView, LetterDetailView, \
    LetterUpdateView, LetterDeleteView, HomeView, toggle_status

app_name = ServiceConfig.name

urlpatterns = [
    path('customer_list/', СustomerListView.as_view(), name='list'),
    path('create/', СustomerCreateView.as_view(), name='create'),
    path('view/<int:pk>/', СustomerDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', СustomerUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', СustomerDeleteView.as_view(), name='delete'),
    path('letter/', LetterListView.as_view(), name='list_letter'),
    path('letter/create/', LetterCreateView.as_view(), name='create_letter'),
    path('letter/view/<int:pk>', LetterDetailView.as_view(), name='view_letter'),
    path('letter/edit/<int:pk>/', LetterUpdateView.as_view(), name='edit_letter'),
    path('letter/delete/<int:pk>/', LetterDeleteView.as_view(), name='delete_letter'),
    path('', HomeView.as_view(), name='logs_list'),
    path('toggle/<int:pk>/', toggle_status, name='toggle_status')

]
