from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    service = models.ForeignKey(Service, related_name='providers', on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.TextField(blank=True)
    availability = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.provider_name
