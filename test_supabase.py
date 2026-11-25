import streamlit as st
from supabase_client import get_diseases

st.title("MedPlus - Supabase Connection Test")

try:
    diseases = get_diseases()

    st.success("Connected to Supabase successfully!")

    st.write("Total diseases retrieved:", len(diseases))

    for disease in diseases:
        st.write(disease["name"])

except Exception as e:
    st.error(f"Connection failed: {e}")