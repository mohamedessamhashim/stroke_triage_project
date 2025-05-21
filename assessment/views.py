# assessment/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # NEW: Import messages for user feedback
from .forms import PatientForm, StrokeAssessmentForm
from .models import Patient, StrokeAssessment # Ensure both models are imported

def patient_list_view(request):
    """
    Displays a list of all registered patients.
    """
    patients = Patient.objects.all().order_by('id') # Changed to order by 'id' ascending
    return render(request, 'assessment/patient_list.html', {'patients': patients})

def patient_form_view(request):
    """
    Handles the display and submission of the PatientForm.
    Upon successful submission, redirects to the stroke assessment form for the new patient.
    """
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save() # Save the new patient object
            # MODIFIED: Redirect directly to the stroke assessment form for the newly created patient
            return redirect('assessment:stroke_assessment_form', patient_id=patient.id)
    else:
        form = PatientForm()
    return render(request, 'assessment/patient_form.html', {'form': form})

def patient_success_view(request, patient_id):
    """
    This view is now primarily for demonstrating the redirect flow.
    New patient submissions will directly redirect from patient_form_view.
    """
    patient = get_object_or_404(Patient, pk=patient_id)
    messages.info(request, f"You are viewing the success page for Patient {patient.id}. Redirecting to patient list.")
    # MODIFIED: Always redirect to the patient list
    return redirect('assessment:patient_list')

def stroke_assessment_form_view(request, patient_id):
    """
    Handles the display and submission of the StrokeAssessmentForm for a specific patient.
    """
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = StrokeAssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False) # Don't save to DB yet
            assessment.patient = patient # Assign the retrieved patient to the assessment
            assessment.save() # Now save the assessment to the database

            # NEW: Add a success message for the user
            messages.success(request, f"Assessment for Patient {patient.id} saved successfully!")
            # MODIFIED: Redirect to the newly created assessment's detail view
            return redirect('assessment:assessment_detail', patient_id=patient.id, assessment_id=assessment.id)
    else:
        form = StrokeAssessmentForm()

    return render(request, 'assessment/stroke_assessment_form.html', {'form': form, 'patient': patient})

def stroke_assessment_success_view(request, patient_id, assessment_id):
    """
    This view is now primarily for demonstrating the redirect flow.
    New assessment submissions will directly redirect from stroke_assessment_form_view.
    """
    patient = get_object_or_404(Patient, pk=patient_id)
    assessment = get_object_or_404(StrokeAssessment, pk=assessment_id, patient=patient)
    messages.info(request, f"You are viewing the success page for Assessment {assessment.id}. Redirecting to assessment details.")
    # MODIFIED: Always redirect to the assessment detail page
    return redirect('assessment:assessment_detail', patient_id=patient.id, assessment_id=assessment.id)

def assessment_detail_view(request, patient_id, assessment_id):
    """
    Displays the details of a specific stroke assessment.
    """
    patient = get_object_or_404(Patient, pk=patient_id)
    assessment = get_object_or_404(StrokeAssessment, pk=assessment_id, patient=patient)
    return render(request, 'assessment/assessment_detail.html', {'patient': patient, 'assessment': assessment})

def patient_delete_view(request, patient_id):
    """
    Handles the deletion of a patient record.
    Displays a confirmation page on GET, deletes on POST.
    """
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        # If the request is POST, it means the user confirmed deletion
        patient.delete()
        messages.success(request, f"Patient ID {patient.id} and all associated assessments have been deleted.")
        return redirect('assessment:patient_list') # Redirect to patient list after deletion
    else:
        # If the request is GET, display the confirmation page
        return render(request, 'assessment/patient_delete_confirm.html', {'patient': patient})
