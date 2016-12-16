from django.contrib.auth.models import Permission, User
from django.db import models
from django.utils import timezone


class Item(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    item_name = models.CharField(max_length=200)
    item_cost = models.CharField(max_length=200)
    item_details = models.TextField()
    item_logo = models.FileField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.item_name
