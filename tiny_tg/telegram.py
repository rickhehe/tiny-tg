import httpx

from .utils import get_telegram_api_key


def send_message(
    chat_id: int | str, 
    text: str,
    timeout: int = 10
) -> bool:

    """
    Send a message to a Telegram chat using the Bot API.
    Args:
        chat_id (int | str): The unique identifier for the target chat or username of the target channel.
        text (str): The message text to send.
        timeout (int, optional): Timeout for the API request in seconds. Defaults to 10.
    Returns:
        bool: True if the message was sent successfully, False otherwise.
    Raises:
        httpx.RequestError: If there was an error with the API request.
    """

    api_key = get_telegram_api_key()
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    
    params = {
        'chat_id': chat_id,
        'text': text
    }
    
    try:
        response = httpx.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        
        result = response.json()
        if result.get('ok'):
            return True
        else:
            return False
            
    except httpx.RequestError as e:
        print(f"✗ Error sending message: {e}")
        raise