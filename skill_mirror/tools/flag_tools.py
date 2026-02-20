# tools/flag_tools.py

def flag_incomplete_evaluation(reason: str, suggestion: str) -> dict:
    """Claude calls this when evaluation cannot proceed normally."""
    print(f"\n⚠️  Agent flagged an issue: {reason}")
    print(f"💡 Suggestion: {suggestion}\n")
    return {
        "flagged": True,
        "reason": reason,
        "suggestion": suggestion
    }