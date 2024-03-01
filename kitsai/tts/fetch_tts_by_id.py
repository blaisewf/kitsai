import requests
from ..token import TokenError, get_api_key

def fetch_tts_by_id(job_id):
    """
    Fetch a Text-to-Speech (TTS) job by its ID from the Arpeggi API.

    Parameters:
    - job_id (str): The ID of the TTS job to fetch.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = f"https://arpeggi.io/api/kits/v1/tts/{job_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error fetching TTS job by ID: {error}")
        return None
