# assessment/urls.py

from django.urls import path
from . import views

app_name = 'assessment'

urlpatterns = [
    # Root path for the assessment app, shows the patient list
    path('', views.patient_list_view, name='patient_list'), # NEW: Root of app shows patient list

    path('patient/new/', views.patient_form_view, name='patient_form'),
    # The patient_success view is now mostly for redirecting, but its URL needs to exist
    path('patient/success/<int:patient_id>/', views.patient_success_view, name='patient_success'),

    path('patient/<int:patient_id>/assessment/new/', views.stroke_assessment_form_view, name='stroke_assessment_form'),
    # The stroke_assessment_success view is now mostly for redirecting
    path('patient/<int:patient_id>/assessment/success/<int:assessment_id>/', views.stroke_assessment_success_view, name='stroke_assessment_success'),
    # NEW: Detail view for a specific assessment
    path('patient/<int:patient_id>/assessment/<int:assessment_id>/', views.assessment_detail_view, name='assessment_detail'),
    path('patient/<int:patient_id>/delete/', views.patient_delete_view, name='patient_delete'),
]
