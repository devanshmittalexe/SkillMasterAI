# tools/question_tools.py


def ask_user_question(question_id: int, topic: str, question_text: str, difficulty: str) -> dict:
    """Present a single question to the user and collect their answer."""
    print(f"\n{'─'*70}")
    print(f"  Question {question_id} | Topic: {topic} | Difficulty: {difficulty.upper()}")
    print(f"{'─'*70}")
    print(f"\n  {question_text}\n")
    answer = input("  Your answer: ").strip()

    return {
        "question_id": question_id,
        "question": question_text,
        "topic": topic,
        "difficulty": difficulty,
        "answer": answer if answer else "[No answer provided]",
        "answered": bool(answer)
    }