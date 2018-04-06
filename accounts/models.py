from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default="This user likes to keep an air of mystery about them.")
    location = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="img/profiles", blank=True, null=True)
    house_number = models.CharField(max_length=20, verbose_name='House number/name *')
    address1 = models.CharField(max_length=60, verbose_name='Street *')
    address2 = models.CharField(max_length=60, blank=True, verbose_name='Secondary address line')
    city = models.CharField(max_length=20, verbose_name='Town/City *')
    county = models.CharField(max_length=30, verbose_name='County/State/Province *')
    post_code = models.CharField(max_length=10, verbose_name='Post/Zip Code *')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
