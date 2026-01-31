import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

# Model selection (change via .env without touching code)
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini").strip()

# Keep fewer messages in memory to reduce token usage
MAX_TURNS_TO_KEEP = int(os.getenv("MAX_TURNS_TO_KEEP", "8"))

# Limit the assistant response length to control cost
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "250"))

# Lower temperature = more stable, less verbose answers
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
