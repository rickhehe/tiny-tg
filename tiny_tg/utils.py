# utils.py
import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Attempt to load .env if it exists (for your Raspberry Pi / Local dev)
# 2. If it doesn't exist, don't raise an error. The OS environment might already have the keys.
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(env_path)

def get_config(key: str, required: bool = True) -> str | None:
    """Get configuration value from environment"""
    value = os.getenv(key)
    if required and not value:
        raise ValueError(f"{key} not found in environment variables. Check .env file.")
    return value

def get_telegram_api_key() -> str:
    """Get Telegram API key from environment"""
    return get_config("TELEGRAM_API_KEY")