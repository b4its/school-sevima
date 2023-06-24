from django.urls import path

from . import views


urlpatterns = [
    path('', views.quiz, name="quiz"),
    path('show', views.nilai_quiz, name="nilai_quiz"),
    path('pertanyaan/<int:id>', views.question, name="question"),
    path('pertanyaan/proses', views.proses, name="proses"),
]