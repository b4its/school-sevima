from django.urls import path

from . import views


urlpatterns = [
    path('', views.quiz, name="quiz"),
    path('pertanyaan/<int:id>', views.question, name="question"),
    path('pertanyaan/proses', views.proses, name="proses"),
]