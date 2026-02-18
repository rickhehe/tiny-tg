"""Command-line interface for tiny-tg."""
import sys
import argparse
from typing import NoReturn

from .telegram import send_message


def main() -> NoReturn:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog='tg',
        description='Send notifications via Telegram'
    )
    
    parser.add_argument('chat_id', help='Telegram chat ID')
    parser.add_argument('text', help='Message text to send')
    parser.add_argument(
        '--timeout',
        type=int,
        default=10,
        help='API request timeout in seconds (default: 10)'
    )
    
    args = parser.parse_args()

    try:
        success = send_message(
            chat_id=args.chat_id,
            text=args.text,
            timeout=args.timeout
        )
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()