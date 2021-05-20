from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class PublisherModel(models.Model):
    username = models.CharField(max_length=15, blank=False)
    bio = models.CharField(max_length=250)
    active = models.BooleanField(default=True)


class UserModel(PublisherModel):
    password = models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthday = models.DateField()
