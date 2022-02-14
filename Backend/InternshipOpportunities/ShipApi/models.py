from django.db import models

# Create your models here.


class InternShip(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    paid = models.BooleanField(default=True)
    stipend = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
