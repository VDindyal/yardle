from django.db import models

# Create your models here.
class Listing(models.Model):
    pub_date = models.DateField(auto_now_add=True)
