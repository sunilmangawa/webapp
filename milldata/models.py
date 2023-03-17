from django.db import models
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=10)
    postal_code = models.IntegerField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Milldata(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"{self.device.name}"