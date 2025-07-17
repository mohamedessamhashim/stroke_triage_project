---
title: 'StrokeTriage: A Django-based Clinical Decision Support Tool for Acute Stroke'
tags:
  - Python
  - Django
  - healthcare
  - stroke
  - clinical decision support
  - NIHSS
  - BE-FAST
  - RACE
  - ASPECTS
authors:
  - name: Mohamed Essam Hashim
    orcid: 0009-0002-9934-2635 
    corresponding: true
    affiliation: 1
affiliations:
 - name: Craniolabs.tech, mohamed@craniolabs.tech
   index: 1
date: 24 May 2025
bibliography: paper.bib

aas-doi: 
aas-journal: 
---

# Summary & Statement of Need

StrokeTriage is a Django-based clinical decision support tool designed to streamline the acute stroke triage process for healthcare providers. It guides users through patient data collection, neurological and imaging assessments, and provides evidence-based treatment recommendations. The tool automates clinical score calculations (NIHSS, BE-FAST, RACE, ASPECTS), eligibility checks, and decision support, all based on current AHA/ASA guidelines [@Powers_etal_2019]. This system is intended for educational, demonstration, and quality improvement purposes, not for direct clinical care.

# Features

- **Patient Registration:** Collects demographics, arrival times, and vital information.
- **Neurological Assessment:** Records BE-FAST+ and Modified NIHSS components.
- **Imaging Findings:** Captures CT scan time, hemorrhage presence, and ASPECTS score.
- **Clinical Score Calculation:** Computes NIHSS [@Brott_etal_1989], mNIHSS [@Lyden_etal_2001], BE-FAST [@Aroor_etal_2017], RACE [@PerezDeLaOssa_etal_2014], and ASPECTS [@Barber_etal_2000].
- **ASPECTS Interpretation:** Provides textual interpretation of the ASPECTS score.
- **Time-Based Eligibility:** Determines tPA and thrombectomy eligibility based on time from Last Known Well.
- **Treatment Recommendations:** Suggests tPA dosing, thrombectomy candidacy, and blood pressure targets.
- **Decision Support:** Recommends stroke center level, transfer guidance, and critical time targets.
- **Sequential Workflow:** Guides users from patient entry to assessment and results.
- **Admin Interface:** Django's built-in admin for data management.

# Mathematics & Clinical Logic

Clinical scores are calculated as the sum of their components. For example, NIHSS is calculated as:
$$
\text{NIHSS} = \sum_{i=1}^{n} \text{component}_i
$$
Each component corresponds to standard NIHSS items [@Brott_etal_1989; @Lyden_etal_2001].

Eligibility logic, such as:

if $\Delta t < 4.5$h and NIHSS $\geq 6$ and no hemorrhage:
  recommend tPA

This mimics the AHA/ASA algorithm [@Powers_etal_2019].

Our tool calculates BE-FAST, RACE, and ASPECTS using validated scoring methods [@Aroor_etal_2017; @PerezDeLaOssa_etal_2014; @Barber_etal_2000].

# Implementation & Usage

StrokeTriage is implemented as a Django web application [@django] and is available as open-source software [@stroke_triage_repo].

**Deployment tip:** Can be run locally (`python manage.py runserver`) or deployed via Docker/Gunicorn for production environments.

# Figures

![Screenshot of stroke assessment form in action.](stroke.png)

# Acknowledgements

We acknowledge the contributions of the open-source Django community and the developers of clinical scoring systems and guidelines that informed this project.

# Disclaimer

This project is for educational and demonstration purposes only. It is not intended for clinical use, diagnosis, treatment, or any medical application. The information and recommendations provided are simplified and should not be used as a substitute for professional medical advice, diagnosis, or treatment. The developer assumes no liability for any actions taken based on the information provided by this application.

# References 