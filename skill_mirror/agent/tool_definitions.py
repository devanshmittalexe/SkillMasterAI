# agent/tool_definitions.py

TOOL_DEFINITIONS = [
    {
        "name": "analyze_topics",
        "description": """Break a subject into 5-8 key subtopics for evaluation.
Call this FIRST to understand what areas to cover.
After calling this, YOU must decide what the actual topics are based on your knowledge.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "description": "The subject to evaluate"
                }
            },
            "required": ["subject"]
        }
    },
    {
        "name": "generate_questions",
        "description": """Generate evaluation questions across topics.
YOU decide the questions based on the topics and your knowledge.
After this tool returns, include your generated questions in the next message.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "topics": {"type": "array", "items": {"type": "string"}},
                "num_questions": {
                    "type": "integer",
                    "description": "How many questions to generate"
                },
                "difficulty_focus": {
                    "type": "string",
                    "enum": ["easy", "medium", "hard", "mixed"],
                    "description": "Difficulty distribution"
                }
            },
            "required": ["subject", "topics", "num_questions"]
        }
    },
    {
        "name": "ask_user_question",
        "description": """Present ONE question to the user and collect their answer.
Call this once per question. You decide when to move to the next question.
If the user gives a blank answer, you can decide whether to move on or probe further.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "question_id": {"type": "integer"},
                "topic": {"type": "string"},
                "question_text": {"type": "string"},
                "difficulty": {
                    "type": "string",
                    "enum": ["easy", "medium", "hard"]
                }
            },
            "required": ["question_id", "topic", "question_text", "difficulty"]
        }
    },
    {
        "name": "grade_answer",
        "description": """Grade a single user answer using your knowledge.
Score 0-10. Provide specific feedback.
YOU are the grader — use your knowledge to evaluate correctness and depth.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "question_id": {"type": "integer"},
                "topic": {"type": "string"},
                "question": {"type": "string"},
                "answer": {"type": "string"},
                "difficulty": {"type": "string"}
            },
            "required": ["question_id", "topic", "question", "answer", "difficulty"]
        }
    },
    {
        "name": "fetch_history",
        "description": """Fetch past evaluation history for a subject.
Call this to compare current performance with previous attempts.
Use this to identify progress trends.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"}
            },
            "required": ["subject"]
        }
    },
    {
        "name": "save_evaluation_result",
        "description": """Save the final evaluation result to persistent storage.
Call this AFTER all grading and analysis is complete.
This must be called before announcing results.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "overall_score": {
                    "type": "number",
                    "description": "Score as percentage 0-100"
                },
                "strong_topics": {"type": "array", "items": {"type": "string"}},
                "weak_topics": {"type": "array", "items": {"type": "string"}},
                "total_questions": {"type": "integer"}
            },
            "required": ["subject", "overall_score", "strong_topics", "weak_topics", "total_questions"]
        }
    },
    {
        "name": "flag_incomplete_evaluation",
        "description": """Flag when the evaluation cannot or should not proceed normally.
Call this if: user answered nothing, all answers are invalid, something unexpected happened.
YOU decide when this is necessary.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "Why the evaluation is incomplete"
                },
                "suggestion": {
                    "type": "string",
                    "description": "What the user should do"
                }
            },
            "required": ["reason", "suggestion"]
        }
    }
]