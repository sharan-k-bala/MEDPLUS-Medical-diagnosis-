
# ==========================================================
# MedPlus - AI Forward Chaining Inference Engine
# Knowledge Base: Supabase Cloud Database
# ==========================================================

from supabase_client import get_knowledge_base


def evaluate_rule(rule, known_facts):

    if "IF" not in rule or "THEN" not in rule:
        return False, [], []

    condition_part = rule.split("IF", 1)[1].split("THEN", 1)[0]

    required = [
        c.strip()
        for c in condition_part.split("AND")
        if c.strip()
    ]

    matched = [c for c in required if c in known_facts]
    missing = [c for c in required if c not in known_facts]

    fired = bool(required) and len(matched) == len(required)

    return fired, matched, missing


def forward_chaining(selected_symptoms):

    knowledge_base = get_knowledge_base()
    known_facts = set(selected_symptoms)
    inferred = []

    for disease, details in knowledge_base.items():

        rule = details.get("rule", "")

        fired, matched, missing = evaluate_rule(
            rule, known_facts
        )

        disease_symptoms = set(details["symptoms"])
        symptom_matches = disease_symptoms.intersection(known_facts)

        if symptom_matches:

            if fired:
                known_facts.add(disease)

            inferred.append({
                "disease": disease,
                "disease_id": details["id"],
                "rule": rule,
                "rule_fired": fired,
                "matched_rule_conditions": matched,
                "missing_rule_conditions": missing,
                "matched_symptoms": sorted(symptom_matches),
                "matched_count": len(symptom_matches),
                "total_symptoms": len(disease_symptoms)
            })

    return inferred


def diagnose(selected_symptoms):

    results = []

    inferred_conditions = forward_chaining(selected_symptoms)

    knowledge_base = get_knowledge_base()

    for item in inferred_conditions:

        disease = item["disease"]
        details = knowledge_base[disease]

        matched = item["matched_count"]
        total = item["total_symptoms"]

        score = (matched / total * 100) if total else 0

        results.append({
            "disease": disease,
            "disease_id": item["disease_id"],
            "score": round(score, 2),
            "matched_symptoms": item["matched_symptoms"],
            "description": details["description"],
            "rule": item["rule"],
            "matched_count": matched,
            "total_symptoms": total,
            "rule_fired": item["rule_fired"],
            "matched_rule_conditions": item["matched_rule_conditions"],
            "missing_rule_conditions": item["missing_rule_conditions"]
        })

    # Prioritise fully satisfied rules, then symptom match
    results.sort(
        key=lambda x: (x["rule_fired"], x["score"]),
        reverse=True
    )

    return results
