from django.db import models

# Create your models here.
class MyProfile(models.Model):
    reg_no = models.TextField(unique=True)
    name = models.TextField()
    email = models.TextField()
    mobile_no = models.TextField(null=True)

