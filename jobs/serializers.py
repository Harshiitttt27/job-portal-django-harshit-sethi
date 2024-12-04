# jobs/serializers.py
from rest_framework import serializers
from .models import JobListing,Company
from users.serializers import CustomUserSerializer



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  # You can also specify fields explicitly like ['id', 'name', 'description', ...]

class JobListingSerializer(serializers.ModelSerializer):
    employer = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = JobListing
        fields = ['id', 'title', 'description', 'location', 'skills_required', 'experience_required', 'posted_at', 'status', 'employer','salary_range', 'job_type','application_deadline',  'remote_option','benefits',
    'contact_email']


# serializers.py
from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job_listing', 'user', 'status', 'applied_at']