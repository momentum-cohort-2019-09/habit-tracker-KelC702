from django.db import models

# Create your models here.


class User(AbstractUser):
    def_str_(self):
        return self.User


class Activity(models.Model):
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    user = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ActivityRecord(models.Model):
    record = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
