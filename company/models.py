# company/models.py

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='company_covers/', blank=True)
    profile_image = models.ImageField(upload_to='company_profiles/', blank=True)
    description = models.TextField(blank=True)
    admins = models.ManyToManyField(User, related_name='admin_companies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'



