# jobs/models.py
from jsonfield import JSONField  # Import JSONField from jsonfield
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills_required = JSONField()  # Using jsonfield.JSONField for skills (non-PostgreSQL databases)
    location = models.CharField(max_length=255)
    experience_required = models.IntegerField()
    posted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('active', 'active'), ('closed', 'closed')])
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_listings',null=True)
    salary_range = models.CharField(max_length=100, blank=True)  # e.g., "$50,000 - $70,000"
    job_type = models.CharField(max_length=50, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('internship', 'Internship')],null=True)
    application_deadline = models.DateTimeField(null=True, blank=True)
    remote_option = models.BooleanField(default=False)
    benefits = models.TextField(blank=True)  # To describe benefits
    contact_email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.title



# models.py
from django.conf import settings  # Import settings
from django.db import models

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]

    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job_listing.title} ({self.status})"