from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    corp_name = models.CharField(max_length=128, null=True, blank=False)
    years_incorporated = models.IntegerField(null=True, blank=False)
    service_cost = models.FloatField(null=True, blank=False)

    CORP_TYPES = (
        ('Construction', 'Construction'),
        ('Financing', 'Financing'),
        ('Property Management', 'Property Management'))
    corp_type = models.CharField(max_length=64, choices=CORP_TYPES, null=True, blank=False)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()