from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class PublisherModel(User): # Como un usuario general:
    bio = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.username


class UserModel(PublisherModel):    # Usuario comun

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    phone = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(blank=True)
    follows = models.ManyToManyField('self', through='FollowRelationship', symmetrical=False, blank=True)


class CompanyModel(PublisherModel):     # Cuenta de empresa

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    apiKey = models.CharField(max_length=50, validators=[MinLengthValidator(50)])


class FollowRelationship(models.Model):     # relacionado con el Id de cada user
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


class PrivateMessageModel(models.Model):
    source = models.ForeignKey(PublisherModel, related_name='source', null=False, blank=False, on_delete=models.SET(get_sentinel_user))
    destination = models.ForeignKey(PublisherModel, related_name='destination', null=False, blank=False, on_delete=models.SET(get_sentinel_user))
    date = models.DateField()
    text = models.CharField(max_length=250)
