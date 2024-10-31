from enum import auto
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """topic to learn"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string"""
        return self.text


class Entry(models.Model):
    """learned things"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class Meta:
    verbose_name_plural = "entries"


def __str__(self):
    """returns string"""
    return f"{self.text[:50]}..."
