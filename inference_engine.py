
# ==========================================================
# MedPlus - AI Forward Chaining Inference Engine
# AI Microproject | Team 8 | Project No. 25
# ==========================================================

from medical_database import KNOWLEDGE_BASE


def evaluate_rule(rule, known_facts):
    """
    Evaluates an IF-THEN rule using partial matching.
    Returns matched and missing conditions.
    """

    if "IF" not in rule or "THEN" not in rule:
        return False, [], []

    condition_part = rule.split("IF", 1)[1].split("THEN", 1)[0]

    required_conditions = [
        condition.strip()
        for condition in condition_part.split("AND")
        if condition.strip()
    ]

    matched_conditions = [
        condition
        for condition in required_conditions
        if condition in known_facts
    ]

    missing_conditions = [
        condition
        for condition in required_conditions
        if condition not in known_facts
    ]

    # Rule fires when all conditions are satisfied
    rule_fired = (
        len(required_conditions) > 0
        and len(matched_conditions) == len(required_conditions)
    )

    return rule_fired, matched_conditions, missing_conditions


def forward_chaining(selected_symptoms):
    """
    Applies forward chaining to patient symptom facts.
    Records fully fired rules and partially matched rules.
    """

    known_facts = set(selected_symptoms)

    inferred_conditions = []

    for disease, details in KNOWLEDGE_BASE.items():

        rule = details.get("rule", "")

        rule_fired, matched_conditions, missing_conditions = (
            evaluate_rule(rule, known_facts)
        )

        disease_symptoms = set(details["symptoms"])

        symptom_matches = disease_symptoms.intersection(
            known_facts
        )

        # Include conditions with at least one symptom match
        if symptom_matches:

            # Fully satisfied rules infer the condition
            if rule_fired:
                known_facts.add(disease)

            inferred_conditions.append({
                "disease": disease,
                "rule": rule,
                "rule_fired": rule_fired,
                "matched_rule_conditions": matched_conditions,
                "missing_rule_conditions": missing_conditions,
                "matched_symptoms": sorted(symptom_matches),
                "matched_count": len(symptom_matches),
                "total_symptoms": len(disease_symptoms)
            })

    return inferred_conditions


def diagnose(selected_symptoms):

    results = []

    # Execute forward chaining
    inferred_conditions = forward_chaining(selected_symptoms)

    # Generate explainable results
    for inferred in inferred_conditions:

        disease = inferred["disease"]

        details = KNOWLEDGE_BASE[disease]

        matched_count = inferred["matched_count"]
        total_symptoms = inferred["total_symptoms"]

        if total_symptoms > 0:
            score = (matched_count / total_symptoms) * 100
        else:
            score = 0

        results.append({
            "disease": disease,
            "score": round(score, 2),
            "matched_symptoms": inferred["matched_symptoms"],
            "description": details.get(
                "description",
                "No description available."
            ),
            "rule": inferred["rule"],
            "matched_count": matched_count,
            "total_symptoms": total_symptoms,
            "rule_fired": inferred["rule_fired"],
            "matched_rule_conditions": inferred[
                "matched_rule_conditions"
            ],
            "missing_rule_conditions": inferred[
                "missing_rule_conditions"
            ]
        })

    # Rank possible conditions by symptom match score
    results.sort(
        key=lambda result: result["score"],
        reverse=True
    )

    return results
