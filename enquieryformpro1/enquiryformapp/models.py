from django.db import models
class EnquiryData(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

