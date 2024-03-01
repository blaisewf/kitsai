import requests
from ..token import TokenError, get_api_key


def create_voice_conversion(
    voice_model_id,
    sound_file,
    backing_sound_file=None,
    conversion_strength=None,
    model_volume_mix=None,
    pitch_shift=None,
    pre=None,
):
    """
    Create a voice conversion and add it to the inference queue via the Arpeggi API.

    Parameters:
    - voice_model_id (int): ID of the voice model.
    - sound_file (file-like object): Sound file to be converted. Supported formats: wav, webm, mp3, or flac. Max file size is 50MB.
    - backing_sound_file (file-like object, optional): Backing sound file. Supported formats: wav, webm, mp3, or flac. Max file size is 50MB.
    - conversion_strength (float, optional): Conversion strength as a percentage (range: 0 - 1).
    - model_volume_mix (float, optional): Model volume mix as a percentage (range: 0 - 1).
    - pitch_shift (int, optional): Pitch shift value (range: -24 to 24).
    - pre (dict, optional): Preprocessing effects.

    Returns:
    - dict or None: JSON response if successful, None otherwise.
    """
    try:
        api_key = get_api_key()
    except TokenError as error:
        raise ValueError(str(error)) from error

    url = "https://arpeggi.io/api/kits/v1/voice-conversions"
    headers = {"Authorization": f"Bearer {api_key}"}

    files = {
        "soundFile": sound_file,
        "voiceModelId": str(voice_model_id),
    }

    data = {
        "conversionStrength": conversion_strength,
        "modelVolumeMix": model_volume_mix,
        "pitchShift": pitch_shift,
        "pre": pre,
    }

    if backing_sound_file:
        files["backingSoundFile"] = backing_sound_file

    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()  # bad responses (4xx or 5xx)
        return response.json()
    except requests.RequestException as error:
        # Log the error and return None
        print(f"Error creating voice conversion: {error}")
        return None
