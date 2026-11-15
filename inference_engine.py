

from medical_database import KNOWLEDGE_BASE


def evaluate_rule(rule, known_facts):
    """
    Evaluates an IF-THEN rule against known facts.
    Uses logical AND conditions.
    """

    if "IF" not in rule or "THEN" not in rule:
        return False, []

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

    rule_fired = (
        len(required_conditions) > 0
        and len(matched_conditions) == len(required_conditions)
    )

    return rule_fired, matched_conditions


def forward_chaining(selected_symptoms):
    """
    Forward chaining:
    Starts with patient symptoms as facts.
    Evaluates rules to infer possible conditions.
    """

    known_facts = set(selected_symptoms)

    inferred_conditions = []

    # Iterate through the knowledge base rules
    for disease, details in KNOWLEDGE_BASE.items():

        rule = details.get("rule", "")

        rule_fired, matched_conditions = evaluate_rule(
            rule,
            known_facts
        )

        if rule_fired:

            # Infer the condition as a new fact
            known_facts.add(disease)

            inferred_conditions.append({
                "disease": disease,
                "rule": rule,
                "matched_rule_conditions": matched_conditions
            })

    return inferred_conditions


def diagnose(selected_symptoms):

    results = []

    user_symptoms = set(selected_symptoms)

    # Apply forward chaining
    inferred_conditions = forward_chaining(selected_symptoms)

    # Generate diagnosis results
    for inferred in inferred_conditions:

        disease = inferred["disease"]

        details = KNOWLEDGE_BASE[disease]

        disease_symptoms = set(details["symptoms"])

        matched_symptoms = disease_symptoms.intersection(
            user_symptoms
        )

        total_symptoms = len(disease_symptoms)
        matched_count = len(matched_symptoms)

        if total_symptoms > 0:
            score = (matched_count / total_symptoms) * 100
        else:
            score = 0

        results.append({
            "disease": disease,
            "score": round(score, 2),
            "matched_symptoms": sorted(matched_symptoms),
            "description": details.get(
                "description",
                "No description available."
            ),
            "rule": inferred["rule"],
            "matched_count": matched_count,
            "total_symptoms": total_symptoms,
            "rule_fired": True,
            "matched_rule_conditions": inferred[
                "matched_rule_conditions"
            ]
        })

    # Rank inferred