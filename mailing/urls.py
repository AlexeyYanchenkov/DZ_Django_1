from django.urls import path
from . import views
from .views import MailingStatsView, MailingCreateView, MailingStatisticsView

app_name = 'mailing'

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('messages/', views.MessageListView.as_view(), name='message_list'),
    path('mailings/', views.MailingListView.as_view(), name='mailing_list'),
    path('stats/', views.MailingStatsView.as_view(), name='stats'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('statistics/', MailingStatisticsView.as_view(), name='mailing_statistics'),
]