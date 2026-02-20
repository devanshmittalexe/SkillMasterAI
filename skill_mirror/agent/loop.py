# agent/loop.py

import json
import anthropic
import os

from config.settings import MODEL, MAX_TOKENS, MAX_ITERATIONS, SYSTEM_PROMPT
from agent.tool_definitions import TOOL_DEFINITIONS
from agent.tool_executor import execute_tool
from dotenv import load_dotenv
load_dotenv()

def run_agent(subject: str, num_questions: int):
    """The agentic loop — Claude decides every step."""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    print(f"\n{'='*70}")
    print("🤖 AUTONOMOUS EVALUATION AGENT".center(70))
    print(f"{'='*70}")
    print(f"\n  Subject: {subject}")
    print(f"  Questions: {num_questions}")
    print(f"\n  Agent is reasoning...\n")

    messages = [
        {
            "role": "user",
            "content": f"Please evaluate me on '{subject}'. Ask me {num_questions} questions."
        }
    ]

    iteration = 0

    while iteration < MAX_ITERATIONS:
        iteration += 1

        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            tools=TOOL_DEFINITIONS,
            messages=messages
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text") and block.text:
                    print(f"\n{'='*70}")
                    print("📢 AGENT REPORT".center(70))
                    print(f"{'='*70}\n")
                    print(block.text)
            print(f"\n{'='*70}\n")
            break

        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"  🔧 Agent calling: {block.name}")

                    result = execute_tool(block.name, block.input)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result)
                    })

            messages.append({"role": "user", "content": tool_results})

        else:
            print(f"  Unexpected stop reason: {response.stop_reason}")
            break

    if iteration >= MAX_ITERATIONS:
        print("\n⚠️  Agent reached maximum iterations limit.")