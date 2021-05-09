from django.urls import path, include
from mpis_backend.views import SektaListView,  maoni, reply, send_message


app_name = 'mpis_backend'
urlpatterns = [
    path('sekta/', SektaListView.as_view(), name='sekta-list'),
    path('maoni/', maoni, name='maoni'),
    path('reply/<pk>/', reply, name='reply'),
    path('send-message/<pk>/', send_message, name='send-msg'),
]
