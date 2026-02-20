from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
print(ANTHROPIC_API_KEY)