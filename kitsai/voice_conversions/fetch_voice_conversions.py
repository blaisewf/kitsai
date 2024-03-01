import requests
from ..token import TokenError, get_api_key

def fetch_voice_conversions(order="asc", page=1, per_page=10):
    """
    Fetch voice conversions from the Arpeggi API.

    Parameters:
    - order (str): Sorting order, either "asc" or "desc".
    - page (int): Page number for pagination.
    - per_page (int): Number of items per page.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = "https://arpeggi.io/api/kits/v1/voice-conversions"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {
        "order": order,
        "page": page,
        "perPage": per_page,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error fetching voice conversions: {error}")
        return None
