# StrokeTriage: A Django-based Clinical Decision Support Tool for Acute Stroke

**Version:** 1.0.0

A comprehensive web application built with Django to assist healthcare providers in making timely decisions for stroke patients based on established medical guidelines. This system guides users through patient information collection, neurological assessments, imaging findings, and provides treatment recommendations.

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Running the Application](#running-the-application)
* [Usage](#usage)
* [Clinical Logic (Simplified)](#clinical-logic-simplified)
* [Disclaimer](#disclaimer)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Features

* **Patient Registration:** Collects essential patient demographics, arrival times, and initial vital information.
* **Neurological Assessment:** Records detailed BE-FAST+ and Modified NIHSS components.
* **Imaging Findings:** Captures CT scan time, presence of hemorrhage, and ASPECTS score.
* **Clinical Score Calculation:** Automatically computes Modified NIHSS total score and RACE score.
* **ASPECTS Interpretation:** Provides textual interpretation of the ASPECTS score.
* **Time-Based Eligibility:** Determines tPA and Thrombectomy eligibility based on time from Last Known Well.
* **Treatment Recommendations:** Suggests tPA dosing, thrombectomy candidacy, and blood pressure management targets.
* **Decision Support:** Recommends stroke center level, transfer guidance, and critical time targets.
* **Sequential Workflow:** Guides users smoothly through patient data entry to assessment and results viewing.
* **Admin Interface:** Django's built-in admin for easy data management.

## Project Structure
```text
.
├── .venv/
├── manage.py
├── assessment/
│   ├── migrations/
│   ├── templates/
│   │   ├── assessment/
│   │   │   ├── patient_form.html
│   │   │   ├── patient_list.html
│   │   │   ├── patient_success.html
│   │   │   ├── stroke_assessment_form.html
│   │   │   ├── stroke_assessment_success.html
│   │   │   ├── assessment_detail.html
│   │   │   └── patient_delete_confirm.html
│   │   └── base.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── stroke_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
└── README.md
...
```


## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/stroke_project.git](https://github.com/yourusername/stroke_project.git) # e.g., [https://github.com/yourusername/stroke_project.git](https://github.com/yourusername/stroke_project.git)
    cd stroke_project
    ```
    *(Note: If your local folder is `django_projects` and the cloned repo is inside it, adjust `cd` accordingly to be in the same directory as `manage.py`)*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows (Command Prompt):
    .\.venv\Scripts\activate
    # On Windows (PowerShell):
    .venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    # Follow the prompts to create a username, email, and password.
    ```

### Running the Application

1.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:8000/assessment/`.

## Usage

* **Home Page (`/assessment/`):** View a list of all registered patients.
* **Add New Patient (`/assessment/patient/new/`):** Enter new patient demographic and initial vital information. Upon submission, you will be automatically redirected to the stroke assessment form for that patient.
* **Add Stroke Assessment (`/assessment/patient/<patient_id>/assessment/new/`):** Fill in detailed neurological assessment, imaging findings, and treatment-related data for a specific patient. Upon submission, you will be redirected to the assessment details page.
* **View Assessment Details (`/assessment/patient/<patient_id>/assessment/<assessment_id>/`):** See a comprehensive overview of a patient's assessment, including calculated scores, eligibility, and decision support.
* **Admin Panel (`/admin/`):** Log in with your superuser account to manage patient and assessment records directly in the Django admin interface.

## Clinical Logic (Simplified)

**IMPORTANT:** The clinical logic implemented in this application (e.g., time windows, scoring, eligibility criteria, BP targets) is **highly simplified for demonstration and educational purposes only.** It is based on general concepts from stroke guidelines but does **NOT** reflect the full complexity, nuances, and exceptions of real-world clinical decision-making.

* **This application is NOT a medical device.**
* **It should NOT be used for actual patient care or to guide clinical decisions.**
* **Always refer to official, validated clinical guidelines and consult with qualified medical professionals for patient management.**

## Disclaimer

This project is created for educational and demonstration purposes only. It is not intended for clinical use, diagnosis, treatment, or any medical application. The information and recommendations provided by this system are simplified and should not be used as a substitute for professional medical advice, diagnosis, or treatment. The developer assumes no liability for any actions taken based on the information provided by this application.

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

Mohamed Essam Hashim, M.B.B.S. - mohamed@craniolabs.tech


