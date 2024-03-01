import requests
from ..token import TokenError, get_api_key

def create_vocal_separation(input_file):
    """
    Create a vocal separation job and add it to the inference queue via the Arpeggi API.

    Parameters:
    - input_file (file-like object): The audio file for which vocal separation is requested. Supported formats: wav, webm, mp3, or flac. Max file size is 50MB.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = "https://arpeggi.io/api/kits/v1/vocal-separations"
    headers = {"Authorization": f"Bearer {api_key}"}

    files = {"inputFile": input_file}

    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error creating vocal separation: {error}")
        return None
