# assessment/admin.py

from django.contrib import admin
from .models import Patient, StrokeAssessment # Import your models

# Register your models here.
# This makes the Patient model visible and manageable in the Django admin interface.
admin.site.register(Patient)

# This makes the StrokeAssessment model visible and manageable in the Django admin interface.
admin.site.register(StrokeAssessment)