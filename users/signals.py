from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveprofile(sender, instance, created, **kwargs):
    instance.profile.save()