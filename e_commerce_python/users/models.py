from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    slug = models.TextField(null=True, blank=True)
    referred_by = models.IntegerField(null=True, blank=True)
    provider = models.CharField(max_length=255, null=True, blank=True)
    provider_id = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(default='customer', max_length=255)
    new_email_verification_code = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    banned = models.SmallIntegerField(default=0)
    referral_code = models.CharField(max_length=255, null=True, blank=True)
    customer_package_id = models.IntegerField(null=True, blank=True)
    remaining_uploads = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username