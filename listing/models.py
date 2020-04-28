from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Listing(models.Model):
    pub_date = models.DateField(auto_now_add=True, null=True, blank=False)
    title = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)

    #Construction
    unit_bedrooms = models.PositiveIntegerField(null=True, blank=False)
    design = models.TextField(null=True, blank=False)
    permit_completed = models.BooleanField(null=True, blank=False)
    foundation_completed = models.BooleanField(null=True, blank=False)
    building_completed = models.BooleanField(null=True, blank=False)

    #Financing
    income = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    assets = models.TextField(null=True, blank=False)
    liabilities = models.TextField(null=True, blank=False)
    down_payment = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)
    interest = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=False)
    financing_secured = models.BooleanField(null=True, blank=False)

    #Get Started
    address = models.TextField(null=True, blank=False)
    backyard_height = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=False)
    backyard_width = models.DecimalField(max_digits=2, decimal_places=2, null=True, blank=False)
    visit_appointment = models.DateField(null=True, blank=False)
    visit_completed = models.BooleanField(null=True, blank=False)

    #Property
    select_property = models.TextField(null=True, blank=False)

