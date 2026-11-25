
REMEDIAL_TIPS = {
    "Common Cold": [
        "Get adequate rest.",
        "Drink plenty of fluids.",
        "Use warm fluids to soothe throat discomfort."
    ],

    "Influenza (Flu)": [
        "Get sufficient rest.",
        "Stay hydrated.",
        "Monitor fever and other symptoms."
    ],

    "Migraine": [
        "Rest in a quiet, dark room.",
        "Maintain regular sleep schedules.",
        "Stay hydrated."
    ],

    "Allergic Rhinitis": [
        "Avoid known allergens.",
        "Keep your surroundings clean.",
        "Reduce exposure to dust and pollen."
    ],

    "Gastroenteritis": [
        "Drink fluids regularly.",
        "Use oral rehydration solution if needed.",
        "Eat light meals as tolerated."
    ],

    "COVID-19": [
        "Rest and stay hydrated.",
        "Monitor your symptoms.",
        "Follow current medical guidance and isolate when advised."
    ],

    "Asthma": [
        "Avoid smoke, dust and known triggers.",
        "Follow your prescribed asthma action plan.",
        "Seek medical help if breathing becomes difficult."
    ],

    "Pneumonia": [
        "Get adequate rest.",
        "Drink sufficient fluids.",
        "Seek prompt medical evaluation."
    ],

    "Diabetes Mellitus": [
        "Monitor blood glucose as advised.",
        "Maintain a balanced diet.",
        "Follow your healthcare professional's treatment plan."
    ],

    "Hypertension": [
        "Reduce excessive salt intake.",
        "Maintain regular physical activity.",
        "Monitor blood pressure regularly."
    ],

    "Dengue": [
        "Drink plenty of fluids.",
        "Get adequate rest.",
        "Seek medical care and avoid aspirin or ibuprofen."
    ],

    "Malaria": [
        "Seek prompt medical diagnosis and treatment.",
        "Stay hydrated.",
        "Take prescribed medication as directed."
    ],

    "Typhoid Fever": [
        "Drink safe, clean water.",
        "Maintain proper food hygiene.",
        "Seek medical treatment promptly."
    ],

    "Bronchitis": [
        "Get sufficient rest.",
        "Drink warm fluids.",
        "Avoid smoking and respiratory irritants."
    ],

    "Tonsillitis": [
        "Drink plenty of fluids.",
        "Try warm salt-water gargles.",
        "Get adequate rest."
    ],

    "UTI": [
        "Drink sufficient water.",
        "Do not delay urination.",
        "Consult a healthcare professional for evaluation."
    ]
}


def get_tips(disease):
    return REMEDIAL_TIPS.get(
        disease,
        ["Consult a qualified healthcare professional."]
    )
