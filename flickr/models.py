from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Flickrgroup(models.Model):

    nsid = models.CharField(max_length=20, primary_key=True)
    group_name = models.CharField(max_length=50, blank = True, null=True)

    def __str__(self):
        return self.nsid

    class Meta:
        verbose_name = "Groups"
        verbose_name_plural = "Flickr Groups"


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nsid = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    group = models.ManyToManyField(Flickrgroup)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.nsid


class Photo(models.Model):

    photo_id = models.CharField(max_length=50, blank = True)
    secret = models.CharField(max_length=50, blank = True)
    server = models.CharField(max_length=50, blank = True)
    farm = models.CharField(max_length=50, blank = True)
    title = models.CharField(max_length=50, blank = True)
    owner_name = models.CharField(max_length=50, blank = True)
    image = models.ImageField(upload_to='images',null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    group = models.ForeignKey(Flickrgroup, blank =True,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.photo_id

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
