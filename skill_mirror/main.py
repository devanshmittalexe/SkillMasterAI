import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
# Make sure your .env or environment variable has ANTHROPIC_API_KEY
api_key = os.environ.get("ANTHROPIC_API_KEY")
# print(api_key)
# if not api_key:
#     raise ValueError("❌ ANTHROPIC_API_KEY not set. Please set it in your environment.")

# client = Anthropic(api_key=api_key)

# # Minimal conversation prompt
# prompt = "\n\nHuman: Hello Claude! Are you working?\n\nAssistant:"

# try:
#     response = client.completions.create(
#         model="claude-haiku-4-5-20251001",
#         prompt=prompt,
#         max_tokens_to_sample=100,
#     )
#     print("\n✅ Claude responded:\n")
#     print(response.completion)

# except Exception as e:
#     print("\n❌ Error communicating with Claude:")
#     print(e)

client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hello Claude, Just checking connection"}
    ]
)

print(response.content[0].text)