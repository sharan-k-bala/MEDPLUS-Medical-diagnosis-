
import streamlit as st
from inference_engine import diagnose
from remedial_tips import get_tips

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="MedPlus | Medical Diagnosis System",
    layout="wide"
)

# ---------------- INITIALIZE DIAGNOSIS RESULTS ----------------

if "diagnosis_results" not in st.session_state:
    st.session_state["diagnosis_results"] = []

if "analysis_completed" not in st.session_state:
    st.session_state["analysis_completed"] = False
# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f5f8fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.header-box {
    background-color: #e8f3fb;
    padding: 25px;
    border-radius: 12px;
    border-left: 6px solid #247ba0;
    margin-bottom: 25px;
}

.header-title {
    color: #164863;
    font-size: 30px;
    font-weight: bold;
}

.header-subtitle {
    color: #526777;
    font-size: 15px;
}

.result-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dce6ef;
    margin-bottom: 15px;
}

.result-title {
    color: #164863;
    font-size: 22px;
    font-weight: bold;
}

.result-description {
    color: #526777;
    font-size: 14px;
}

.footer {
    text-align: center;
    color: #7b8794;
    font-size: 13px;
    padding-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.html(
    """
    <div style="
        background: linear-gradient(135deg, #16324f, #245b78);
        padding: 30px;
        border-radius: 15px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 20px;
    ">
        <div style="
            background: white;
            color: #245b78;
            font-size: 35px;
            font-weight: bold;
            padding: 12px 20px;
            border-radius: 12px;
        ">
            +
        </div>

        <div>
            <h1 style="color: white; margin: 0;">MedPlus</h1>
            <p style="color: #d7e9f5; margin: 5px 0;">
                Medical Diagnosis Knowledge Representation System
            </p>
            <p style="color: #d7e9f5; margin: 0;">
                AI-powered rule-based symptom analysis
            </p>
        </div>
    </div>
    """,
)
# ---------------- SIDEBAR ----------------

st.sidebar.title("Patient Assessment")

st.sidebar.write(
    "Select the symptoms currently experienced by the patient."
)

symptom_options = {
    # General Symptoms
    "Fever": "fever",
    "Body Pain": "body_pain",
    "Headache": "headache",
    "Severe Headache": "severe_headache",
    "Fatigue": "fatigue",
    "Dizziness": "dizziness",
    "Chills": "chills",
    "Sweating": "sweating",

    # Respiratory Symptoms
    "Cough": "cough",
    "Dry Cough": "dry_cough",
    "Mild Cough": "mild_cough",
    "Runny Nose": "runny_nose",
    "Sneezing": "sneezing",
    "Sore Throat": "sore_throat",
    "Wheezing": "wheezing",
    "Shortness of Breath": "shortness_of_breath",
    "Chest Tightness": "chest_tightness",
    "Chest Pain": "chest_pain",
    "Nasal Congestion": "nasal_congestion",

    # Digestive Symptoms
    "Nausea": "nausea",
    "Vomiting": "vomiting",
    "Diarrhea": "diarrhea",
    "Stomach Pain": "stomach_pain",
    "Lower Abdominal Pain": "lower_abdominal_pain",

    # Neurological and Other Symptoms
    "Sensitivity to Light": "sensitivity_to_light",
    "Blurred Vision": "blurred_vision",
    "Itchy Eyes": "itchy_eyes",
    "Skin Rash": "skin_rash",
    "Loss of Taste": "loss_of_taste",
    "Loss of Smell": "loss_of_smell",
    "Difficulty Swallowing": "difficulty_swallowing",

    # Metabolic and Urinary Symptoms
    "Frequent Urination": "frequent_urination",
    "Increased Thirst": "increased_thirst",
    "Increased Hunger": "increased_hunger",
    "Painful Urination": "painful_urination"
}

selected_labels = st.sidebar.multiselect(
    "Symptoms",
    options=list(symptom_options.keys())
)

selected_symptoms = [
    symptom_options[label]
    for label in selected_labels
]

st.sidebar.markdown("---")

diagnose_button = st.sidebar.button(
    "🔍 Analyze Symptoms",
    use_container_width=True
)

clear_button = st.sidebar.button(
    "🔄 Clear Selection",
    use_container_width=True
)

if clear_button:
    st.rerun()

# ---------------- MAIN CONTENT ----------------

st.subheader("System Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Knowledge Base**\n\nStores disease information and associated symptoms.")

with col2:
    st.info("**Inference Engine**\n\nApplies rule-based reasoning to analyze symptoms.")

with col3:
    st.info("**Diagnosis Output**\n\nDisplays possible conditions based on symptom matches.")

st.markdown("---")




# ---------------- PATIENT ASSESSMENT SUMMARY ----------------

diagnosis_results = st.session_state.get("diagnosis_results") or []

conditions_count = len(diagnosis_results)

top_condition = (
    diagnosis_results[0]["disease"]
    if diagnosis_results
    else "--"
)

analysis_status = (
    "Analyzed"
    if st.session_state.get("analysis_completed", False)
    else "Ready"
)

# Summary Header
st.markdown("""
<div style="
    background: linear-gradient(135deg, #16324f, #245b78);
    padding: 22px;
    border-radius: 15px;
    margin-bottom: 20px;
">
    <h2 style="color: white; margin: 0;">
        📋 Patient Assessment Summary
    </h2>
    <p style="color: #d7e9f5; margin: 5px 0 0 0;">
        Overview of the selected symptoms and system analysis
    </p>
</div>
""", unsafe_allow_html=True)

# Summary Metrics
summary_col1, summary_col2, summary_col3, summary_col4 = st.columns(4)

with summary_col1:
    st.metric(
        label="Symptoms Selected",
        value=len(selected_symptoms)
    )

with summary_col2:
    st.metric(
        label="Assessment Status",
        value=analysis_status
    )

with summary_col3:
    st.metric(
        label="Conditions Identified",
        value=conditions_count
    )

with summary_col4:
    st.metric(
        label="Top-Ranked Condition",
        value=top_condition
    )

# Selected Symptoms
st.markdown("### 📝 Selected Symptoms")

if selected_labels:

    symptom_text = " • ".join(selected_labels)

    st.markdown(
        f"""
        <div style="
            background-color: #172b3d;
            border: 1px solid #31516b;
            padding: 16px;
            border-radius: 10px;
            color: #eaf4fc;
            font-size: 16px;
        ">
            {symptom_text}
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.info(
        "No symptoms selected. Please select symptoms from the sidebar."
    )

st.markdown("---")






# ---------------- DIAGNOSIS RESULTS ----------------

st.subheader("Diagnosis Results")

if diagnose_button:

    if not selected_symptoms:

        st.warning("Please select at least one symptom.")

        st.session_state["diagnosis_results"] = []
        st.session_state["analysis_completed"] = False

    else:

        results = diagnose(selected_symptoms) or []

        # Store results in session state
        st.session_state["diagnosis_results"] = results
        st.session_state["analysis_completed"] = True

        # Refresh the application to update summary metrics
        st.rerun()


# Display stored diagnosis results
diagnosis_results = st.session_state.get("diagnosis_results", [])

if diagnosis_results:

    st.subheader(" Analysis Results")

    for result in diagnosis_results:

     with st.expander(
        f"🔍 {result['disease']} — "
        f"Symptom Match: {result['score']}%"
    ):

        st.write("### 🧠 AI Reasoning Explanation")

        st.success("✅ IF–THEN Rule Fired: All rule conditions satisfied.")

        st.write("**Knowledge-Based Rule:**")
        st.code(result["rule"])

        st.write("**Conditions Satisfied:**")

        for condition in result.get("matched_rule_conditions", []):
            st.success(condition.replace("_", " ").title())

        st.write("**Symptoms Matched:**")

        for symptom in result["matched_symptoms"]:
            st.success(symptom.replace("_", " ").title())

        st.write(
            f"**Symptom Match:** {result['matched_count']} "
            f"out of {result['total_symptoms']} symptoms"
        )

        st.progress(int(result["score"]))

        st.write("### 💡 Recommended Care")

        for tip in get_tips(result["disease"]):
            st.info(tip)

else:
     if st.session_state.get("analysis_completed", False):
        st.warning(
            "No conditions matched the selected symptoms. "
            "Try selecting additional symptoms."
        )
     else:
        st.info(
            "Select symptoms and click Analyze Symptoms to view results."
         )