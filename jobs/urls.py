# jobs/urls.py
from django.urls import path, include
from .views import JobListingCreateView,JobListingDetailView,ApplicationCreateView,ApplicationStatusView,ApplicationWithdrawView,ApplicationListView,JobSearchView,CompanyListCreateView,CompanyDetailView
from rest_framework.routers import DefaultRouter






urlpatterns = [
    path('companies', CompanyListCreateView.as_view(), name="list-create-company"),

    # URL for retrieving, updating, and deleting a specific company (GET, PUT, DELETE)
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name="company-detail"),

    # URL for creating a new job listing (POST)
    path('createjob', JobListingCreateView.as_view(), name='job-listing-create'),

    # URL for retrieving a single job listing by pk (GET)
    path('job-listings', JobListingDetailView.as_view(), name='job-listing-detail'),
    path('job-listings/<int:pk>/', JobListingDetailView.as_view(), name='job-listing-detail'),

    # URL for updating a job listing (PUT)
    path('update/job-listings/<int:pk>/', JobListingDetailView.as_view(), name='job-listing-update'),

    # URL for partially updating a job listing (PATCH)
    path('partial-update/job-listings/<int:pk>/', JobListingDetailView.as_view(), name='job-listing-partial-update'),

    # URL for deleting a job listing (DELETE)
    path('delete/job-listings/<int:pk>/', JobListingDetailView.as_view(), name='job-listing-delete'),
    
    # URL for creating a new application/apply job (POST)
    path('jobs/<int:job_listing_id>/apply/', ApplicationCreateView.as_view(), name='apply-job'),

    #URL for getting applications (GET)
    path('applications/', ApplicationListView.as_view(), name='list-applications'),

    #URL for withdrawing application (DELETE)
    path('applications/<int:application_id>/withdraw/', ApplicationWithdrawView.as_view(), name='withdraw-application'),

    #URL for checking status of job (GET)
    path('applications/<int:application_id>/status/', ApplicationStatusView.as_view(), name='application-status'),

    #URL for searching jobs (GET)
    path('jobs/search/', JobSearchView.as_view(), name='search-jobs'),

]

