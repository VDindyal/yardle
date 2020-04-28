from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Construction
    unit_bedrooms = models.PositiveIntegerField()
    design = models.TextField()
    permit_completed = models.BooleanField()
    foundation_completed = models.BooleanField()
    building_completed = models.BooleanField()

    #Financing
    income = models.DecimalField(max_digits=6, decimal_places=2)
    assets = models.TextField()
    liabilities = models.TextField()
    down_payment = models.DecimalField(max_digits=6, decimal_places=2)
    interest = models.DecimalField(max_digits=2, decimal_places=2)
    financing_secured = models.BooleanField()

    #Get Started
    address = models.TextField()
    backyard_height = models.DecimalField(max_digits=2, decimal_places=2)
    backyard_width = models.DecimalField(max_digits=2, decimal_places=2)
    visit_appointment = models.DateField()
    visit_completed = models.BooleanField()

    #Property
    select_property = models.TextField()

