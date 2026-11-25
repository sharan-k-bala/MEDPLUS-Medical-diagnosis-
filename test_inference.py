import streamlit as st
from inference_engine import diagnose

st.title("MedPlus - Cloud Inference Test")

symptoms = [
    "fever",
    "body_pain",
    "fatigue"
]

try:
    results = diagnose(symptoms)

    st.success("Cloud inference engine working!")

    for result in results:
        st.write(
            result["disease"],
            result["score"],
            "Rule Fired:", result["rule_fired"]
        )

except Exception as e:
    st.error(str(e))