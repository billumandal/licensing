from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
import time

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ip_addr = models.GenericIPAddressField(protocol='both')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

def _createHash():
    hash_2 = hashlib.sha1()
    hash_2.update(str(time.time()))
    return hash_2.hexdigest()[:-10]

class Name(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=150)
    hash_1 = models.CharField(max_length=30, default=_createHash, unique=True)

    def __unicode__(self):
        return self.name