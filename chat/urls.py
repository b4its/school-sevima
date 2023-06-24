from django.urls import path

from . import views


urlpatterns = [
    path('chat', views.chat, name="chat"),
    path('chat/proses', views.proses_chat, name="proses_chat"),
    path('chat/delete', views.cleaner, name="cleaner"),
]