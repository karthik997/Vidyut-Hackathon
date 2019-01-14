from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.name