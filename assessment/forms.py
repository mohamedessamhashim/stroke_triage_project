# assessment/forms.py

from django import forms
from .models import Patient, StrokeAssessment

class PatientForm(forms.ModelForm):
    """
    Form for collecting initial patient demographic, vital, and medication information.
    """
    class Meta:
        model = Patient 
        fields = [
            'arrival_time',
            'last_known_well_time',
            'age',
            'weight_kg',
            'systolic_bp',
            'diastolic_bp',
            'blood_glucose',
            'anticoagulant_status',
            'anticoagulant_medication',
            'last_anticoagulant_dose',
        ]
        # Widgets for better user experience, especially for DateTimeField
        widgets = {
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'last_known_well_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'last_anticoagulant_dose': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        # Labels or help text if different from model's help_text
        labels = {
            'weight_kg': 'Weight (kg)',
            'systolic_bp': 'Systolic BP (mmHg)',
            'diastolic_bp': 'Diastolic BP (mmHg)',
            'blood_glucose': 'Blood Glucose',
        }
        help_texts = {
            'blood_glucose': 'Enter blood glucose in mg/dL or mmol/L.',
        }

class StrokeAssessmentForm(forms.ModelForm):
    """
    Form for collecting detailed neurological assessment data.
    """
    class Meta:
        model = StrokeAssessment
        fields = [
            # Link to Patient is handled in the view, not directly in the form
            'be_fast_balance',
            'be_fast_eyes',
            'be_fast_face_drooping',
            'be_fast_arm_weakness',
            'be_fast_speech_difficulty',
            'be_fast_time_to_call',
            'be_fast_plus_other',
            'nihss_1a_loc_alert',
            'nihss_1b_loc_questions',
            'nihss_1c_loc_commands',
            'nihss_2_best_gaze',
            'nihss_3_visual_field',
            'nihss_4_facial_palsy',
            'nihss_5a_motor_left_arm',
            'nihss_5b_motor_right_arm',
            'nihss_6a_motor_left_leg',
            'nihss_6b_motor_right_leg',
            'nihss_7_limb_ataxia',
            'nihss_8_sensory',
            'nihss_9_best_language',
            'nihss_10_dysarthria',
            'nihss_11_extinction_inattention',
            'ct_scan_time',
            'hemorrhage_present',
            'aspects_score',
            'lvo_status',
            'lvo_location',
            'tpa_eligibility',
            'thrombectomy_eligibility',
            'treatment_recommendation',
            'ct_scan_time',
            'hemorrhage_present',
            'aspects_score',
            'lvo_status',
            'lvo_location',
            'recent_surgery',
            'prior_stroke_head_trauma',
            'gi_urinary_hemorrhage',
            'low_platelets',
            'elevated_inr',
            'current_anticoagulant_use',
        ]
        widgets = {
            'ct_scan_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'be_fast_balance': 'BE-FAST: Balance',
            'be_fast_eyes': 'BE-FAST: Eyes',
            'be_fast_face_drooping': 'BE-FAST: Face Drooping',
            'be_fast_arm_weakness': 'BE-FAST: Arm Weakness',
            'be_fast_speech_difficulty': 'BE-FAST: Speech Difficulty',
            'be_fast_time_to_call': 'BE-FAST: Time to Call',
            'be_fast_plus_other': 'BE-FAST+: Other Symptoms (Headache/Confusion)',
            'nihss_1a_loc_alert': 'NIHSS 1a: LOC Alertness (0-3)',
            'nihss_1b_loc_questions': 'NIHSS 1b: LOC Questions (0-2)',
            'nihss_1c_loc_commands': 'NIHSS 1c: LOC Commands (0-2)',
            'nihss_2_best_gaze': 'NIHSS 2: Best Gaze (0-2)',
            'nihss_3_visual_field': 'NIHSS 3: Visual Field (0-3)',
            'nihss_4_facial_palsy': 'NIHSS 4: Facial Palsy (0-3)',
            'nihss_5a_motor_left_arm': 'NIHSS 5a: Motor Left Arm (0-4, X)',
            'nihss_5b_motor_right_arm': 'NIHSS 5b: Motor Right Arm (0-4, X)',
            'nihss_6a_motor_left_leg': 'NIHSS 6a: Motor Left Leg (0-4, X)',
            'nihss_6b_motor_right_leg': 'NIHSS 6b: Motor Right Leg (0-4, X)',
            'nihss_7_limb_ataxia': 'NIHSS 7: Limb Ataxia (0-2, UN)',
            'nihss_8_sensory': 'NIHSS 8: Sensory (0-2, UN)',
            'nihss_9_best_language': 'NIHSS 9: Best Language (0-3, UN)',
            'nihss_10_dysarthria': 'NIHSS 10: Dysarthria (0-2, UN)',
            'nihss_11_extinction_inattention': 'NIHSS 11: Extinction & Inattention (0-2)',
            'ct_scan_time': 'CT Scan Time',
            'hemorrhage_present': 'Hemorrhage Present on Imaging',
            'aspects_score': 'ASPECTS Score (0-10)',
            'lvo_status': 'Large Vessel Occlusion Status',
            'lvo_location': 'LVO Location',
            'tpa_eligibility': 'tPA Eligibility',
            'thrombectomy_eligibility': 'Thrombectomy Eligibility',
            'treatment_recommendation': 'Treatment Recommendation',
            'recent_surgery': 'Recent Major Surgery/Trauma (last 3 months)',
            'prior_stroke_head_trauma': 'Prior Stroke/Head Trauma (last 3 months)',
            'gi_urinary_hemorrhage': 'Recent GI/Urinary Hemorrhage (within 21 days)',
            'low_platelets': 'Platelet Count < 100,000/mm³',
            'elevated_inr': 'INR > 1.7',
            'current_anticoagulant_use': 'Current Anticoagulant Use',
        }
        help_texts = {
            'aspects_score': 'Lower score indicates more severe ischemia.',
            'lvo_location': 'e.g., ICA, M1, M2. Leave blank if LVO Absent/Unknown.',
            'treatment_recommendation': 'Provide a summary of recommended treatment based on guidelines.',
        }