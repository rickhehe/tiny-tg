# utils.py
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Load .env file once at module level
env_path = find_dotenv()
if env_path:
    load_dotenv(env_path)
else:
    raise FileNotFoundError(
        "No .env file found. Please create a .env file in the project root with required configuration."
    )

def get_config(key: str, required: bool = True) -> str | None:
    """Get configuration value from environment"""
    value = os.getenv(key)
    if required and not value:
        raise ValueError(f"{key} not found in environment variables. Check .env file.")
    return value

def get_telegram_api_key() -> str:
    """Get Telegram API key from environment"""
    return get_config("TELEGRAM_API_KEY")