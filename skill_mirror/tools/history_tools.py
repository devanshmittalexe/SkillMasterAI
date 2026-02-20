# tools/history_tools.py

import json
import os
from datetime import datetime
from config.settings import HISTORY_FILE


def save_evaluation_result(subject: str, overall_score: float, strong_topics: list,
                            weak_topics: list, total_questions: int) -> dict:
    """Persist evaluation result to history file."""
    history = {}

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        except Exception:
            history = {}

    subject_history = history.get(subject, [])
    subject_history.append({
        "timestamp": datetime.now().isoformat(),
        "score": overall_score,
        "strong_topics": strong_topics,
        "weak_topics": weak_topics,
        "total_questions": total_questions
    })
    history[subject] = subject_history

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    return {
        "saved": True,
        "subject": subject,
        "total_attempts": len(subject_history),
        "all_scores": [h["score"] for h in subject_history]
    }


def fetch_history(subject: str) -> dict:
    """Retrieve past evaluation history for a subject."""
    if not os.path.exists(HISTORY_FILE):
        return {"subject": subject, "attempts": [], "total_attempts": 0}

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
        subject_history = history.get(subject, [])
        return {
            "subject": subject,
            "attempts": subject_history,
            "total_attempts": len(subject_history),
            "scores": [h["score"] for h in subject_history],
            "best_score": max((h["score"] for h in subject_history), default=None),
            "average_score": round(
                sum(h["score"] for h in subject_history) / len(subject_history), 1
            ) if subject_history else None
        }
    except Exception as e:
        return {"subject": subject, "error": str(e), "attempts": []}