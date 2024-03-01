import requests
from ..token import TokenError, get_api_key


def fetch_voice_models(
    order="asc", page=1, per_page=10, my_models=False, instruments=False
):
    """
    Fetch voice models from the Arpeggi API.

    Parameters:
    - order (str): Sorting order, either "asc" or "desc".
    - page (int): Page number for pagination.
    - per_page (int): Number of items per page.
    - my_models (bool): Whether to fetch only user's models.
    - instruments (bool): Whether to include instrument details.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = "https://arpeggi.io/api/kits/v1/voice-models"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {
        "order": order,
        "page": page,
        "perPage": per_page,
        "myModels": str(my_models).lower(),
        "instruments": str(instruments).lower(),
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error fetching voice models: {error}")
        return None
