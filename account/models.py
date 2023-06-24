from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User 
# Create your models here.\




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    sekolah = models.CharField(blank=True,null=True,max_length=100)
    asal_kota = models.CharField(blank=True,null=True,max_length=100)
    no_telpon = models.CharField(blank=True,null=True,max_length = 50)
    token = models.CharField(blank=True,null=True,max_length=300)
    def __str__(self):
        return f"{self.user.username}', {self.user.first_name} {self.user.last_name} {self.token}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
