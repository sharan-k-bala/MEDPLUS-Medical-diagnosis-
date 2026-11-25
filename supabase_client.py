
import streamlit as st
from supabase import create_client


@st.cache_resource
def get_supabase_client():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )


@st.cache_data(ttl=300)
def get_knowledge_base():

    db = get_supabase_client()

    diseases = db.table("diseases").select("*").execute().data
    symptoms = db.table("symptoms").select("*").execute().data
    mappings = db.table("disease_symptoms").select("*").execute().data

    symptom_lookup = {
        s["id"]: s["name"] for s in symptoms
    }

    knowledge = {}

    for disease in diseases:
        knowledge[disease["name"]] = {
            "id": disease["id"],
            "description": disease["description"],
            "rule": disease["diagnostic_rule"],
            "symptoms": []
        }

    for mapping in mappings:
        disease = next(
            (d for d in diseases if d["id"] == mapping["disease_id"]),
            None
        )

        if disease:
            symptom = symptom_lookup.get(mapping["symptom_id"])

            if symptom:
                knowledge[disease["name"]]["symptoms"].append(symptom)

    return knowledge


def get_diseases():
    return (
        get_supabase_client()
        .table("diseases")
        .select("*")
        .execute()
        .data
    )


def get_symptoms():
    return (
        get_supabase_client()
        .table("symptoms")
        .select("*")
        .execute()
        .data
    )


def get_remedial_tips(disease_id):

    response = (
        get_supabase_client()
        .table("remedial_tips")
        .select("tip")
        .eq("disease_id", disease_id)
        .execute()
    )

    return [item["tip"] for item in response.data]
