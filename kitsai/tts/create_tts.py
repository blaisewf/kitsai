import requests
from ..token import TokenError, get_api_key


def create_tts(voice_model_id, input_tts_text):
    """
    Create a Text-to-Speech (TTS) job and add it to the inference queue via the Arpeggi API.

    Parameters:
    - voice_model_id (int): ID of the voice model.
    - input_tts_text (str): Text to be converted to speech.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = "https://arpeggi.io/api/kits/v1/tts"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"voiceModelId": voice_model_id, "inputTtsText": input_tts_text}

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error creating TTS job: {error}")
        return None
