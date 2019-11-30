# This file contains visitor model for this project

from django.db import models
from host.models import Host


class Visitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=10)
    address_Visited = models.TextField()
    checkInTime = models.DateTimeField(auto_now_add=True)
    IS_VISITOR_CHECKED_IN = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    is_checked_in = models.CharField(max_length=3, choices=IS_VISITOR_CHECKED_IN, default='Yes')
    checkoutTime = models.DateTimeField(auto_now=True)
    # checkoutTime automatically updates when
    # visitor checks out from checkout from
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    # Foreign key is used to link every visitor with a host

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
