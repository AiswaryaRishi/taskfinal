from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('credentials:dept',args=[self.name])


class Courses(models.Model):
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    duration=models.IntegerField()

    def __str__(self):
        return self.name

