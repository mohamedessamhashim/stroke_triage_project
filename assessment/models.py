# assessment/models.py

from django.db import models
from django.utils import timezone # NEW: Import timezone for working with datetimes
from datetime import timedelta   # NEW: Import timedelta for calculating time differences


# Define the Patient model
class Patient(models.Model):
    """
    This represents a patient in the stroke assessment system.
    This stores initial demographic and medical history information.
    """
    # Patient Identification and Timings
    # auto_now_add=True sets the time automatically when the object is first created
    arrival_time = models.DateTimeField(
        help_text="Time of patient's arrival at the facility."
    )
    # blank=True and null=True allow this field to be empty in the database
    last_known_well_time = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Last time the patient was known to be at their baseline state."
    )

    # Basic Demographics
    age = models.IntegerField(
        help_text="Patient's age in years."
    )
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Patient's weight in kilograms."
    )

    # Vital Signs and Basic Medical Info
    systolic_bp = models.IntegerField(
        help_text="Systolic blood pressure (mmHg)."
    )
    diastolic_bp = models.IntegerField(
        help_text="Diastolic blood pressure (mmHg)."
    )
    blood_glucose = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Blood glucose level (e.g., mg/dL or mmol/L - specify units as needed)."
    )

    # Anticoagulant Information
    anticoagulant_status_choices = [
        ('NONE', 'None'),
        ('CURRENT', 'Currently on anticoagulant'),
        ('RECENT', 'Recent anticoagulant use (within 48 hours)'),
        ('UNKNOWN', 'Unknown'),
    ]
    anticoagulant_status = models.CharField(
        max_length=10,
        choices=anticoagulant_status_choices,
        default='UNKNOWN',
        help_text="Anticoagulant use status."
    )
    anticoagulant_medication = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Specific anticoagulant medication (if applicable)."
    )
    last_anticoagulant_dose = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Date and time of last anticoagulant dose (if applicable)."
    )

    # This method defines how a Patient object is represented as a string.
    # It's very useful for displaying objects in the Django admin and other places.
    def __str__(self):
        return f"Patient (Age: {self.age}, Arrival: {self.arrival_time.strftime('%Y-%m-%d %H:%M')})"

    # Meta class for model options (e.g., ordering, verbose names)
    class Meta:
        verbose_name = "Patient Record"
        verbose_name_plural = "Patient Records"
        ordering = ['-arrival_time'] # Order patients by most recent arrival first

class StrokeAssessment(models.Model):
    """
    Represents a detailed stroke assessment for a specific patient.
    Links to the Patient model and includes various clinical and imaging findings.
    """
    # Link to the Patient model (One-to-Many relationship: one patient can have many assessments)
    # on_delete=models.CASCADE means if a Patient is deleted, all their assessments are also deleted.
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='assessments', # Allows accessing assessments from a patient object: patient.assessments.all()
        help_text="The patient associated with this assessment."
    )

    # Assessment Timings (for this specific assessment)
    assessment_time = models.DateTimeField(
        auto_now_add=True, # Automatically sets the time when the assessment is created
        help_text="Time when this assessment was recorded."
    )

    # BE-FAST+ Assessment Components (Boolean fields for Yes/No)
    # blank=True allows the field to be left empty in forms
    # null=True allows the field to be stored as NULL in the database
    # default=False provides a default value if not specified
    be_fast_balance = models.BooleanField(
        default=False,
        help_text="Sudden loss of balance or coordination."
    )
    be_fast_eyes = models.BooleanField(
        default=False,
        help_text="Sudden blurred vision or loss of vision in one or both eyes."
    )
    be_fast_face_drooping = models.BooleanField(
        default=False,
        help_text="Face drooping or numbness on one side."
    )
    be_fast_arm_weakness = models.BooleanField(
        default=False,
        help_text="Arm weakness or numbness in one arm."
    )
    be_fast_speech_difficulty = models.BooleanField(
        default=False,
        help_text="Speech difficulty or slurred speech."
    )
    be_fast_time_to_call = models.BooleanField(
        default=False,
        help_text="Time to call emergency services (sudden onset of any symptom)."
    )
    be_fast_plus_other = models.BooleanField(
        default=False,
        help_text="Other sudden severe headache or confusion."
    )

    # Modified NIHSS Components (Integer fields, ranges can be handled in forms/validation)
    nihss_1a_loc_alert = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 1a: Level of Consciousness (Alertness)."
    )
    nihss_1b_loc_questions = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 1b: Level of Consciousness (Questions)."
    )
    nihss_1c_loc_commands = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 1c: Level of Consciousness (Commands)."
    )
    nihss_2_best_gaze = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 2: Best Gaze."
    )
    nihss_3_visual_field = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 3: Visual Field."
    )
    nihss_4_facial_palsy = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 4: Facial Palsy."
    )
    nihss_5a_motor_left_arm = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 5a: Motor Left Arm."
    )
    nihss_5b_motor_right_arm = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 5b: Motor Right Arm."
    )
    nihss_6a_motor_left_leg = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 6a: Motor Left Leg."
    )
    nihss_6b_motor_right_leg = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 6b: Motor Right Leg."
    )
    nihss_7_limb_ataxia = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 7: Limb Ataxia."
    )
    nihss_8_sensory = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 8: Sensory."
    )
    nihss_9_best_language = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 9: Best Language."
    )
    nihss_10_dysarthria = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 10: Dysarthria."
    )
    nihss_11_extinction_inattention = models.IntegerField(
        blank=True, null=True,
        help_text="NIHSS 11: Extinction and Inattention."
    )

    # Imaging Findings
    ct_scan_time = models.DateTimeField(
        blank=True, null=True,
        help_text="Time of CT scan completion."
    )
    hemorrhage_present = models.BooleanField(
        default=False,
        help_text="Indicates if hemorrhage is present on imaging."
    )
    aspects_score = models.IntegerField(
        blank=True, null=True,
        help_text="ASPECTS score (0-10) for ischemic changes. Lower score indicates more severe ischemia."
    )

    # Large Vessel Occlusion (LVO) Details
    lvo_status_choices = [
        ('NOT_ASSESSED', 'Not Assessed'),
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('UNKNOWN', 'Unknown'),
    ]
    lvo_status = models.CharField(
        max_length=15,
        choices=lvo_status_choices,
        default='NOT_ASSESSED',
        help_text="Status of Large Vessel Occlusion."
    )
    lvo_location = models.CharField(
        max_length=100,
        blank=True, null=True,
        help_text="Location of LVO (e.g., ICA, M1, M2)."
    )
    # These are boolean fields indicating presence of a contraindication
    recent_surgery = models.BooleanField(
        default=False,
        help_text="Major surgery or serious trauma in the last 3 months."
    )
    prior_stroke_head_trauma = models.BooleanField(
        default=False,
        help_text="History of prior stroke or serious head trauma in the last 3 months."
    )
    gi_urinary_hemorrhage = models.BooleanField(
        default=False,
        help_text="Recent gastrointestinal or urinary tract hemorrhage (within 21 days)."
    )
    low_platelets = models.BooleanField(
        default=False,
        help_text="Platelet count < 100,000/mm³."
    )
    elevated_inr = models.BooleanField(
        default=False,
        help_text="INR > 1.7 (if on warfarin or other anticoagulants)."
    )
    current_anticoagulant_use = models.BooleanField(
        default=False,
        help_text="Current use of direct thrombin inhibitors or factor Xa inhibitors."
    )
    # Treatment Decisions and Eligibility
    tpa_eligibility_choices = [
        ('ELIGIBLE', 'Eligible'),
        ('NOT_ELIGIBLE', 'Not Eligible'),
        ('CONTRAINDICATED', 'Contraindicated'),
        ('PENDING', 'Pending Assessment'),
    ]
    tpa_eligibility = models.CharField(
        max_length=15,
        choices=tpa_eligibility_choices,
        default='PENDING',
        help_text="Eligibility for tPA (tissue plasminogen activator)."
    )
    thrombectomy_eligibility_choices = [
        ('ELIGIBLE', 'Eligible'),
        ('NOT_ELIGIBLE', 'Not Eligible'),
        ('CONTRAINDICATED', 'Contraindicated'),
        ('PENDING', 'Pending Assessment'),
    ]
    thrombectomy_eligibility = models.CharField(
        max_length=15,
        choices=thrombectomy_eligibility_choices,
        default='PENDING',
        help_text="Eligibility for mechanical thrombectomy."
    )
    treatment_recommendation = models.TextField(
        blank=True, null=True,
        help_text="Recommended treatment plan based on guidelines."
    )

    def calculate_time_since_lkw(self):
        """
        Calculates the time difference between the patient's last_known_well_time
        and the current assessment_time.
        Returns a timedelta object or None if LKW time is not available.
        """
        # Ensure both LKW time and assessment time are available for calculation
        if self.patient.last_known_well_time and self.assessment_time:
            # Calculate the difference. Django's DateTimeField stores timezone-aware datetimes.
            return self.assessment_time - self.patient.last_known_well_time
        return None

    def get_time_since_lkw_hours(self):
        """
        Returns the time since last known well in hours, rounded to two decimal places.
        Returns None if LKW time is not available or calculation fails.
        """
        time_delta = self.calculate_time_since_lkw()
        if time_delta:
            # Convert timedelta to total seconds and then to hours
            return round(time_delta.total_seconds() / 3600, 2)
        return None

    def is_within_tpa_window(self):
        """
        Checks if the patient is within the tPA treatment window.
        Simplified rule: within 4.5 hours from Last Known Well time.
        Returns False if LKW time is not available.
        """
        hours_since_lkw = self.get_time_since_lkw_hours()
        if hours_since_lkw is not None and hours_since_lkw <= 4.5:
            return True
        return False

    def is_within_thrombectomy_window(self):
        """
        Checks if the patient is within the mechanical thrombectomy treatment window.
        Simplified rule: within 6 hours from Last Known Well time.
        Returns False if LKW time is not available.
        """
        hours_since_lkw = self.get_time_since_lkw_hours()
        if hours_since_lkw is not None and hours_since_lkw <= 6:
            return True
        return False

    def calculate_nihss_total_score(self):
        """
        Calculates the total Modified NIHSS score by summing relevant components.
        Returns the total score or None if essential components are missing.
        """
        # List of NIHSS fields to sum. Use .get() with a default of 0 to handle None values gracefully.
        # NIHSS scores are typically integers, so sum them directly.
        nihss_components = [
            self.nihss_1a_loc_alert,
            self.nihss_1b_loc_questions,
            self.nihss_1c_loc_commands,
            self.nihss_2_best_gaze,
            self.nihss_3_visual_field,
            self.nihss_4_facial_palsy,
            self.nihss_5a_motor_left_arm,
            self.nihss_5b_motor_right_arm,
            self.nihss_6a_motor_left_leg,
            self.nihss_6b_motor_right_leg,
            self.nihss_7_limb_ataxia,
            self.nihss_8_sensory,
            self.nihss_9_best_language,
            self.nihss_10_dysarthria,
            self.nihss_11_extinction_inattention,
        ]

        total_score = 0
        for component in nihss_components:
            # Only add if the component has a value (is not None)
            if component is not None:
                total_score += component
            else:
                # If any core NIHSS component is missing, return None for total score
                # as a complete score cannot be calculated.
                return None
        return total_score

    def calculate_race_score(self):
        """
        Calculates the RACE score for LVO prediction based on specific NIHSS components.
        RACE Score Components (simplified for demonstration):
        - Facial Palsy (NIHSS 4): 0=0, 1=1, 2=2, 3=2 (max 2)
        - Arm Motor (NIHSS 5a/5b): 0=0, 1=0, 2=1, 3=1, 4=2 (max 2 for worse arm)
        - Leg Motor (NIHSS 6a/6b): 0=0, 1=0, 2=1, 3=1, 4=2 (max 2 for worse leg)
        - Gaze (NIHSS 2): 0=0, 1=1, 2=2 (max 2)
        - Aphasia (NIHSS 9): 0=0, 1=0, 2=1, 3=2 (max 2)
        - Agnosia (NIHSS 11): 0=0, 1=1, 2=2 (max 2)
        Total RACE score ranges from 0-9.
        """
        race_score = 0

        # Facial Palsy (NIHSS 4)
        if self.nihss_4_facial_palsy is not None:
            if self.nihss_4_facial_palsy == 1: race_score += 1
            elif self.nihss_4_facial_palsy >= 2: race_score += 2

        # Arm Motor (NIHSS 5a/5b) - take the worse score
        arm_motor_score = 0
        if self.nihss_5a_motor_left_arm is not None and self.nihss_5b_motor_right_arm is not None:
            worse_arm = max(self.nihss_5a_motor_left_arm, self.nihss_5b_motor_right_arm)
            if worse_arm >= 2: arm_motor_score = 1
            if worse_arm >= 4: arm_motor_score = 2 # Score 4 is for no movement
        elif self.nihss_5a_motor_left_arm is not None:
            if self.nihss_5a_motor_left_arm >= 2: arm_motor_score = 1
            if self.nihss_5a_motor_left_arm >= 4: arm_motor_score = 2
        elif self.nihss_5b_motor_right_arm is not None:
            if self.nihss_5b_motor_right_arm >= 2: arm_motor_score = 1
            if self.nihss_5b_motor_right_arm >= 4: arm_motor_score = 2
        race_score += arm_motor_score

        # Leg Motor (NIHSS 6a/6b) - take the worse score
        leg_motor_score = 0
        if self.nihss_6a_motor_left_leg is not None and self.nihss_6b_motor_right_leg is not None:
            worse_leg = max(self.nihss_6a_motor_left_leg, self.nihss_6b_motor_right_leg)
            if worse_leg >= 2: leg_motor_score = 1
            if worse_leg >= 4: leg_motor_score = 2
        elif self.nihss_6a_motor_left_leg is not None:
            if self.nihss_6a_motor_left_leg >= 2: leg_motor_score = 1
            if self.nihss_6a_motor_left_leg >= 4: leg_motor_score = 2
        elif self.nihss_6b_motor_right_leg is not None:
            if self.nihss_6b_motor_right_leg >= 2: leg_motor_score = 1
            if self.nihss_6b_motor_right_leg >= 4: leg_motor_score = 2
        race_score += leg_motor_score

        # Gaze (NIHSS 2)
        if self.nihss_2_best_gaze is not None:
            if self.nihss_2_best_gaze == 1: race_score += 1
            elif self.nihss_2_best_gaze == 2: race_score += 2

        # Aphasia (NIHSS 9)
        if self.nihss_9_best_language is not None:
            if self.nihss_9_best_language >= 2: race_score += 2 # Score 2 or 3 for aphasia

        # Agnosia (NIHSS 11) - Extinction and Inattention
        if self.nihss_11_extinction_inattention is not None:
            if self.nihss_11_extinction_inattention >= 1: race_score += 1 # Score 1 or 2 for agnosia

        # If any relevant NIHSS component is None, we cannot calculate a complete RACE score.
        # You might choose to return None or a partial score depending on clinical requirements.
        # For simplicity, if any required component is None, we'll return None.
        required_race_components = [
            self.nihss_4_facial_palsy,
            self.nihss_5a_motor_left_arm, self.nihss_5b_motor_right_arm,
            self.nihss_6a_motor_left_leg, self.nihss_6b_motor_right_leg,
            self.nihss_2_best_gaze,
            self.nihss_9_best_language,
            self.nihss_11_extinction_inattention,
        ]
        if any(c is None for c in required_race_components):
             return None # Cannot calculate full RACE score if components are missing

        return race_score

    def get_aspects_interpretation(self):
        """
        Provides a textual interpretation of the ASPECTS score.
        ASPECTS (Alberta Stroke Program Early CT Score) ranges from 0-10.
        - 10: Normal CT
        - 8-9: Mild ischemia
        - 5-7: Moderate ischemia
        - 0-4: Severe ischemia, typically contraindication for IV thrombolysis/thrombectomy
        """
        if self.aspects_score is None:
            return "ASPECTS score not available."
        elif self.aspects_score == 10:
            return "Normal CT scan (no early ischemic changes)."
        elif self.aspects_score >= 8: # 8 or 9
            return "Mild early ischemic changes."
        elif self.aspects_score >= 5: # 5, 6, or 7
            return "Moderate early ischemic changes."
        elif self.aspects_score >= 0: # 0, 1, 2, 3, or 4
            return "Severe early ischemic changes (significant infarction)."
        else:
            return "Invalid ASPECTS score."
        
    def get_tpa_eligibility_status(self):
        """
        Determines overall tPA eligibility based on time window and contraindications.
        Returns a string indicating eligibility status.
        """
        # Check for time window
        if not self.is_within_tpa_window():
            return "Not Eligible (Outside Time Window)"

        # Check for major contraindications
        if self.hemorrhage_present:
            return "Contraindicated (Intracranial Hemorrhage)"
        if self.patient.systolic_bp is not None and self.patient.systolic_bp > 185:
            return "Contraindicated (BP > 185 mmHg)"
        if self.patient.diastolic_bp is not None and self.patient.diastolic_bp > 110:
            return "Contraindicated (BP > 110 mmHg)"
        if self.recent_surgery or self.prior_stroke_head_trauma or self.gi_urinary_hemorrhage:
            return "Contraindicated (Major Bleeding Risk Factors)"
        if self.low_platelets:
            return "Contraindicated (Low Platelets)"
        if self.elevated_inr:
            return "Contraindicated (Elevated INR)"
        if self.current_anticoagulant_use:
            return "Contraindicated (Current Anticoagulant Use)"
        # Add other contraindications as needed based on guidelines

        # If within time window and no contraindications
        return "Potentially Eligible"

    def calculate_tpa_dose(self):
        """
        Calculates the tPA dose based on patient weight (0.9 mg/kg, max 90mg).
        Returns the calculated dose in mg, or None if weight is missing.
        """
        if self.patient.weight_kg is not None:
            calculated_dose = float(self.patient.weight_kg) * 0.9
            # Max dose is 90mg
            return min(calculated_dose, 90.0)
        return None

    def get_thrombectomy_candidacy(self):
        """
        Assesses thrombectomy candidacy based on time window, LVO status, and ASPECTS.
        Simplified rules:
        - Within 6-hour window (already checked by is_within_thrombectomy_window)
        - LVO present
        - ASPECTS score >= 6 (common threshold, but varies)
        Returns a string indicating candidacy.
        """
        if not self.is_within_thrombectomy_window():
            return "Not Candidate (Outside Time Window)"

        if self.hemorrhage_present:
            return "Not Candidate (Intracranial Hemorrhage)"

        if self.lvo_status != 'PRESENT':
            return "Not Candidate (No LVO Detected)"

        if self.aspects_score is None:
            return "Pending (ASPECTS Score Missing)"
        elif self.aspects_score < 6: # Threshold for poor outcome/contraindication
            return "Not Candidate (ASPECTS < 6)"

        return "Potentially Candidate"

    def get_bp_management_target(self):
        """
        Provides blood pressure management targets based on treatment eligibility.
        Simplified guidelines:
        - If tPA eligible: BP < 185/110 mmHg
        - If thrombectomy candidate (without tPA): BP < 185/110 mmHg (or other specific target)
        - Otherwise: BP < 220/120 mmHg
        Returns a string with the target.
        """
        tpa_eligibility = self.get_tpa_eligibility_status()
        thrombectomy_candidacy = self.get_thrombectomy_candidacy()

        if tpa_eligibility == "Potentially Eligible":
            return "Target BP < 185/110 mmHg (for tPA)"
        elif thrombectomy_candidacy == "Potentially Candidate":
            # If thrombectomy candidate but not tPA eligible (e.g., outside tPA window)
            return "Target BP < 185/110 mmHg (for thrombectomy)"
        else:
            return "Target BP < 220/120 mmHg (permissive hypertension)"
    def get_stroke_center_recommendation(self):
        """
        Recommends the appropriate level of stroke center based on assessment findings.
        Simplified logic based on LVO candidacy and NIHSS.
        """
        thrombectomy_candidacy = self.get_thrombectomy_candidacy()
        nihss_score = self.calculate_nihss_total_score()

        if thrombectomy_candidacy == "Potentially Candidate":
            return "Comprehensive Stroke Center (CSC) recommended for thrombectomy."
        elif nihss_score is not None and nihss_score >= 5: # Example threshold for moderate-severe stroke
            return "Primary Stroke Center (PSC) recommended for IV thrombolysis and stroke care."
        else:
            return "Acute Stroke Ready Hospital (ASRH) or general hospital for initial stabilization."

    def get_transfer_recommendation(self):
        """
        Provides transfer recommendations based on stroke center needs.
        Simplified logic: if CSC recommended, suggest transfer if not already at one.
        """
        center_recommendation = self.get_stroke_center_recommendation()
        # This assumes the system doesn't know the current facility's capability.
        # In a real system, you'd have a field for 'current_facility_type'.
        if "Comprehensive Stroke Center (CSC)" in center_recommendation:
            return "Consider immediate transfer to a Comprehensive Stroke Center (CSC) for advanced care."
        elif "Primary Stroke Center (PSC)" in center_recommendation:
            return "Consider transfer to a Primary Stroke Center (PSC) if not at one."
        else:
            return "No immediate transfer recommended based on current findings."

    def get_critical_time_targets(self):
        """
        Provides critical time targets based on AHA/ASA guidelines.
        These are ideal targets, not actual elapsed times.
        """
        targets = {}
        if self.patient.arrival_time:
            # Door-to-CT/Imaging: ideally within 20 minutes of arrival
            targets['Door-to-CT Target'] = (self.patient.arrival_time + timedelta(minutes=20)).strftime('%H:%M')

            # Door-to-Needle (tPA) Target: ideally within 60 minutes of arrival
            targets['Door-to-Needle (tPA) Target'] = (self.patient.arrival_time + timedelta(minutes=60)).strftime('%H:%M')

            # Door-to-Groin Puncture (Thrombectomy) Target: ideally within 90 minutes of arrival
            targets['Door-to-Groin Puncture Target'] = (self.patient.arrival_time + timedelta(minutes=90)).strftime('%H:%M')

        return targets

    # String representation of the object
    def __str__(self):
        return f"Assessment for Patient ID: {self.patient.id} at {self.assessment_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Stroke Assessment"
        verbose_name_plural = "Stroke Assessments"
        ordering = ['-assessment_time'] # Order assessments by most recent first