from django.db import models


class RequestLog(models.Model):
    ip_address = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    device_name = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} request from {self.ip_address} at {self.timestamp}"
