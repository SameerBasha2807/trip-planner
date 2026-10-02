def validate_plan(output: str) -> dict:
    text = output.lower()

    checks = {
        "has_days": "day 1" in text,
        "has_budget": "budget" in text,
        "has_transport": "transport" in text,
        "structure_valid": any(x in output for x in ["##", "-", "•"]),
    }

    checks["all_passed"] = all(checks.values())
    return checks