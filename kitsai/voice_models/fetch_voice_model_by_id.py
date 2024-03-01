import requests
from ..token import TokenError, get_api_key


def fetch_voice_model_by_id(model_id):
    """
    Fetch a voice model by its ID from the Arpeggi API.

    Parameters:
    - model_id (str): The ID of the voice model to fetch.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = f"https://arpeggi.io/api/kits/v1/voice-models/{model_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error fetching voice model by ID: {error}")
        return None
