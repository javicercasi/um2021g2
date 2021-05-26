from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model


# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class PublisherModel(models.Model):
    username = models.CharField(max_length=15, blank=False)
    bio = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=True)


class UserModel(PublisherModel):
    password = models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True)
    follows = models.ManyToManyField('self', through='FollowRelationship', symmetrical=False, blank=True)


class FollowRelationship(models.Model):
    from_user = models.ForeignKey(UserModel, related_name='from_user', on_delete=models.SET(get_sentinel_user))
    to_user = models.ForeignKey(UserModel, related_name='to_user', on_delete=models.SET(get_sentinel_user))

    class Meta:
        unique_together = ('from_user', 'to_user')


class TagModel(models.Model):
    name = models.CharField(max_length=15)
    ocurrencies = models.IntegerField()


class PublicMessageModel(models.Model):
    author = models.ForeignKey(PublisherModel, related_name='author', null=False, blank=False, on_delete=models.SET(get_sentinel_user))
    text = models.CharField(max_length=140)
    date = models.DateField()
    mentions = models.ManyToManyField(PublisherModel, related_name='mentions', blank=True)
    tags = models.ManyToManyField(TagModel, blank=True)
