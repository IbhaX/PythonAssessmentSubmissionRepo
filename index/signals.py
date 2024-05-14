from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from index.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a Profile when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)