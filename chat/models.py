from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Kunci(models.Model):
    kata_kunci = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.kata_kunci}'
    
class Jawaban(models.Model):
    kunci = models.ForeignKey(Kunci, on_delete = models.CASCADE)
    penjelasan = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.penjelasan}'

class Bot_ai(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    kunci = models.ForeignKey(Kunci, on_delete = models.CASCADE)
    penjelasan = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.kunci.kata_kunci}| {self.penjelasan}'

class Pengguna(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pertanyaan = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}| {self.pertanyaan}'

