from django.db import models
from django.contrib.auth.models import User

# Create your models here.

benar = (
	('A','A'),
	('B','B'),
	('C','C'),
    ('D','D'),
)

class Kategori(models.Model):
    nama = models.CharField(max_length=500)
    image = models.ImageField(upload_to='kategori/icon',blank=True,null=True)
    penjelasan = models.CharField(max_length=500, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nama}'
    
class Pertanyaan(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete = models.CASCADE)
    bobot = models.IntegerField(blank=True,null=True,default=1)
    question = models.CharField(max_length=1000,blank=True,null=True)
    pilihan_a = models.CharField(max_length=800,blank=True,null=True)
    pilihan_b = models.CharField(max_length=800,blank=True,null=True)
    pilihan_c = models.CharField(max_length=800,blank=True,null=True)
    pilihan_d = models.CharField(max_length=800,blank=True,null=True)
    jawaban_benar = models.CharField(max_length=100,blank=True,null=True,choices=benar)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.kategori}|{self.question}'

class Hasil(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    kategori = models.ForeignKey(Kategori,blank=True,null=True, on_delete = models.CASCADE)
    total_nilai = models.CharField(max_length=100,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.total_nilai}| {self.created}'