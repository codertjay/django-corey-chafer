from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# this signal is automatically creating a profile for a new user


""" everything here is linked for u to see something like this meams i dont understand """


@receiver(post_save, sender=User)
def Create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def Save_profile(sender, instance, **kwargs):
    instance.profile.save()
