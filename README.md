# tiny-tg

[![PyPI version](https://badge.fury.io/py/tiny-tg.svg)](https://badge.fury.io/py/tiny-tg)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, lightweight Python library for sending Telegram notifications. Perfect for automation scripts, server monitoring, and quick alerts.

## Features

- 🚀 **Simple** - One command to send messages
- 📦 **Tiny** - Minimal dependencies (just `httpx` and `python-dotenv`)
- 🔧 **Flexible** - Use as CLI tool or Python library
- ⚡ **Fast** - Direct API calls, no bloat
- 🐍 **Modern** - Python 3.11+ with type hints

## Installation

### As a Library (for Python projects)

```bash
# Using uv (recommended)
uv add tiny-tg
```

### As a CLI Tool (system-wide)

```bash
# Using uv (recommended - isolated environment)
uv tool install tiny-tg
```

After `uv tool install`, the `tg` command is available globally without activating a virtual environment.

## Setup

1. **Create a Telegram Bot:**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the prompts
   - Copy your API token

2. **Get Your Chat ID:**
   - Message [@userinfobot](https://t.me/userinfobot) to get your chat ID
   - Or message your bot and visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

3. **Configure Environment:**

Create a `.env` file in your project root:

```env
TELEGRAM_API_KEY=your_bot_token_here
```

## Usage

### Command Line

```bash
# Send a message
tg CHAT_ID "Hello from tiny-tg!"

# With custom timeout
tg CHAT_ID "Server is down!" --timeout 30
```

### Python API

```python
from tiny_tg import send_message

# Send a notification
send_message(
    chat_id=123456789,
    text="Deployment complete! ✅"
)

# With custom timeout
send_message(
    chat_id=123456789,
    text="Critical alert!",
    timeout=30
)
```

## Examples

### Cron Job Notifications

```bash
# Daily reminder at 09:00
0 9 * * * /path/to/venv/bin/tg 123456789 "Daily backup complete"
```

### Script Integration

```python
from tiny_tg import send_message

def backup_database():
    try:
        # ... backup logic ...
        send_message(123456789, "✅ Backup successful")
    except Exception as e:
        send_message(123456789, f"❌ Backup failed: {e}")
```

### Server Monitoring

```python
import psutil
from tiny_tg import send_message

CHAT_ID = 123456789

# Check disk space
disk = psutil.disk_usage('/')
if disk.percent > 90:
    send_message(CHAT_ID, f"⚠️ Disk usage: {disk.percent}%")
```

### Raspberry Pi Alerts

```python
from tiny_tg import send_message
import subprocess

def check_temperature():
    temp = subprocess.check_output(['vcgencmd', 'measure_temp'])
    temp_c = float(temp.decode().split('=')[1].split("'")[0])
    
    if temp_c > 70:
        send_message(123456789, f"🌡️ High temp: {temp_c}°C")

check_temperature()
```

### Project Structure

```
tiny-tg/
├── tiny_tg/
│   ├── __init__.py      # Package exports
│   ├── telegram.py      # Core messaging logic
│   ├── utils.py         # Config utilities
│   └── cli.py           # Command-line interface
├── pyproject.toml       # Project configuration
├── .env                 # API credentials (gitignored)
└── README.md
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `TELEGRAM_API_KEY` | Yes | Your Telegram bot token from @BotFather |

### Function Parameters

#### `send_message(chat_id, text, timeout=10)`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `chat_id` | `int \| str` | - | Telegram chat ID or username |
| `text` | `str` | - | Message text to send |
| `timeout` | `int` | `10` | Request timeout in seconds |

**Returns:** `bool` - `True` if successful, `False` otherwise

**Raises:** `httpx.RequestError` - If the API request fails

## Requirements

- Python 3.11+
- `httpx` - Modern HTTP client
- `python-dotenv` - Environment variable management

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## Links

- **Homepage:** https://github.com/rickhehe/tiny-tg
- **Issues:** https://github.com/rickhehe/tiny-tg/issues
- **PyPI:** https://pypi.org/project/tiny-tg/

---

Keep it simple.  
Make it happen.  