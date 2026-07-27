import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# LEETCODE CONSTANTS
LEETCODE_API_URL = "https://leetcode.com/graphql"
DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

# OpenAI Configuration
OPENAI_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.3  # Lower = more deterministic, better for code

# Validation
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is not set in .env file")

print("✅ Configuration loaded successfully")
