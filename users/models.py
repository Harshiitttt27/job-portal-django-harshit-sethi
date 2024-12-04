# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Custom field for profile picture
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Custom field for role (Employer, Job Seeker, Admin, etc.)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')

    # Custom field for phone number
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Avoid reverse accessor clashes by setting a unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set_groups',  # Unique reverse accessor for CustomUser.groups
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Unique reverse accessor for CustomUser.user_permissions
        blank=True
    )

    def __str__(self):
        return self.username


from django.db import models

class BlacklistedToken(models.Model):
    token = models.CharField(max_length=512)  # Store the token here
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when token was blacklisted

    def __str__(self):
        return self.token

























































































































































































