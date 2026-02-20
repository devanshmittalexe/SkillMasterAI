# agent/tool_executor.py

from tools.topic_tools import analyze_topics, generate_questions
from tools.question_tools import ask_user_question
from tools.grading_tools import grade_answer
from tools.history_tools import fetch_history, save_evaluation_result
from tools.flag_tools import flag_incomplete_evaluation


TOOLS_MAP = {
    "analyze_topics": analyze_topics,
    "generate_questions": generate_questions,
    "ask_user_question": ask_user_question,
    "grade_answer": grade_answer,
    "fetch_history": fetch_history,
    "save_evaluation_result": save_evaluation_result,
    "flag_incomplete_evaluation": flag_incomplete_evaluation,
}


def execute_tool(tool_name: str, tool_input: dict):
    """Route Claude's tool call to the actual Python function."""
    tool_fn = TOOLS_MAP.get(tool_name)

    if not tool_fn:
        return {"error": f"Unknown tool: {tool_name}"}

    return tool_fn(**tool_input)