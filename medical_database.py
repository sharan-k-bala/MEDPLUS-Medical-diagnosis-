
# ==========================================================
# MediLogic - Medical Diagnosis Knowledge Base
# AI Microproject | Team 8 | Project No. 25
# Educational prototype only
# ==========================================================

KNOWLEDGE_BASE = {

    "Common Cold": {
        "symptoms": [
            "runny_nose",
            "sneezing",
            "sore_throat",
            "mild_cough"
        ],
        "description": (
            "A common viral infection affecting the nose and throat. "
            "It may cause sneezing, runny nose, and mild cough."
        ),
        "rule": (
            "IF runny_nose AND sneezing AND sore_throat "
            "THEN Common Cold"
        )
    },

    "Influenza (Flu)": {
        "symptoms": [
            "fever",
            "body_pain",
            "headache",
            "cough",
            "fatigue"
        ],
        "description": (
            "A viral respiratory infection that may cause fever, "
            "body pain, headache, cough, and fatigue."
        ),
        "rule": (
            "IF fever AND body_pain AND fatigue "
            "THEN Influenza"
        )
    },

    "Migraine": {
        "symptoms": [
            "severe_headache",
            "nausea",
            "sensitivity_to_light"
        ],
        "description": (
            "A neurological condition that can cause severe headache, "
            "nausea, and sensitivity to light."
        ),
        "rule": (
            "IF severe_headache AND nausea "
            "AND sensitivity_to_light THEN Migraine"
        )
    },

    "Allergic Rhinitis": {
        "symptoms": [
            "sneezing",
            "runny_nose",
            "itchy_eyes",
            "nasal_congestion"
        ],
        "description": (
            "An allergic condition that commonly causes sneezing, "
            "runny nose, itchy eyes, and nasal congestion."
        ),
        "rule": (
            "IF sneezing AND itchy_eyes AND runny_nose "
            "THEN Allergic Rhinitis"
        )
    },

    "Gastroenteritis": {
        "symptoms": [
            "diarrhea",
            "vomiting",
            "stomach_pain",
            "fever"
        ],
        "description": (
            "An inflammation of the stomach and intestines "
            "that may cause vomiting, diarrhea, and stomach pain."
        ),
        "rule": (
            "IF diarrhea AND vomiting AND stomach_pain "
            "THEN Gastroenteritis"
        )
    },

    "COVID-19": {
        "symptoms": [
            "fever",
            "dry_cough",
            "fatigue",
            "loss_of_taste",
            "loss_of_smell"
        ],
        "description": (
            "A viral respiratory illness caused by SARS-CoV-2. "
            "Symptoms may include fever, cough, and fatigue."
        ),
        "rule": (
            "IF fever AND dry_cough AND fatigue "
            "THEN Possible COVID-19"
        )
    },

    "Asthma": {
        "symptoms": [
            "wheezing",
            "shortness_of_breath",
            "chest_tightness",
            "cough"
        ],
        "description": (
            "A respiratory condition involving inflammation "
            "and narrowing of the airways."
        ),
        "rule": (
            "IF wheezing AND shortness_of_breath "
            "AND chest_tightness THEN Possible Asthma"
        )
    },

    "Pneumonia": {
        "symptoms": [
            "fever",
            "cough",
            "shortness_of_breath",
            "chest_pain",
            "fatigue"
        ],
        "description": (
            "An infection of the lungs that may cause fever, "
            "cough, chest pain, and breathing difficulty."
        ),
        "rule": (
            "IF fever AND cough AND shortness_of_breath "
            "THEN Possible Pneumonia"
        )
    },

    "Diabetes Mellitus": {
        "symptoms": [
            "frequent_urination",
            "increased_thirst",
            "increased_hunger",
            "fatigue"
        ],
        "description": (
            "A metabolic condition involving elevated blood glucose. "
            "Diagnosis requires appropriate blood glucose testing."
        ),
        "rule": (
            "IF frequent_urination AND increased_thirst "
            "THEN Consider Diabetes Screening"
        )
    },

    "Hypertension": {
        "symptoms": [
            "headache",
            "dizziness",
            "blurred_vision"
        ],
        "description": (
            "A condition characterized by persistently elevated "
            "blood pressure. It often has no noticeable symptoms."
        ),
        "rule": (
            "IF suspected hypertension THEN measure blood pressure"
        )
    },

    "Dengue": {
        "symptoms": [
            "fever",
            "severe_headache",
            "body_pain",
            "nausea",
            "skin_rash"
        ],
        "description": (
            "A mosquito-borne viral infection that may cause "
            "fever, severe headache, body pain, and rash."
        ),
        "rule": (
            "IF fever AND body_pain AND severe_headache "
            "THEN Consider Dengue Evaluation"
        )
    },

    "Malaria": {
        "symptoms": [
            "fever",
            "chills",
            "sweating",
            "headache",
            "fatigue"
        ],
        "description": (
            "A mosquito-borne parasitic disease that may cause "
            "fever, chills, sweating, and fatigue."
        ),
        "rule": (
            "IF fever AND chills AND sweating "
            "THEN Consider Malaria Evaluation"
        )
    },

    "Typhoid Fever": {
        "symptoms": [
            "fever",
            "headache",
            "stomach_pain",
            "fatigue",
            "diarrhea"
        ],
        "description": (
            "A bacterial infection that may cause prolonged fever, "
            "headache, stomach pain, and digestive symptoms."
        ),
        "rule": (
            "IF fever AND headache AND stomach_pain "
            "THEN Consider Typhoid Evaluation"
        )
    },

    "Bronchitis": {
        "symptoms": [
            "cough",
            "mild_cough",
            "chest_tightness",
            "fatigue"
        ],
        "description": (
            "Inflammation of the bronchial tubes that may cause "
            "cough, chest discomfort, and fatigue."
        ),
        "rule": (
            "IF cough AND chest_tightness "
            "THEN Possible Bronchitis"
        )
    },

    "Tonsillitis": {
        "symptoms": [
            "sore_throat",
            "fever",
            "headache",
            "difficulty_swallowing"
        ],
        "description": (
            "Inflammation of the tonsils that may cause "
            "sore throat, fever, and difficulty swallowing."
        ),
        "rule": (
            "IF sore_throat AND fever AND difficulty_swallowing "
            "THEN Possible Tonsillitis"
        )
    },

    "Urinary Tract Infection (UTI)": {
        "symptoms": [
            "frequent_urination",
            "painful_urination",
            "lower_abdominal_pain"
        ],
        "description": (
            "An infection affecting parts of the urinary system "
            "that may cause painful and frequent urination."
        ),
        "rule": (
            "IF painful_urination AND frequent_urination "
            "THEN Consider UTI Evaluation"
        )
    }
}
