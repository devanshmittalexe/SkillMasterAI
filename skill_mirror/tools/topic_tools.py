# tools/topic_tools.py


def analyze_topics(subject: str) -> dict:
    """Break a subject into key evaluation subtopics."""
    return {
        "subject": subject,
        "status": "awaiting_llm_decomposition",
        "instruction": f"Decompose '{subject}' into 5-8 key subtopics for evaluation."
    }


def generate_questions(subject: str, topics: list, num_questions: int, difficulty_focus: str = "mixed") -> dict:
    """Generate evaluation questions across topics."""
    return {
        "subject": subject,
        "topics": topics,
        "num_questions": num_questions,
        "difficulty_focus": difficulty_focus,
        "status": "awaiting_llm_generation",
        "instruction": "Generate questions now using your knowledge."
    }