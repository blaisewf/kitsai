# Unofficial [Kits.AI](https://kits.ai) API Implementation

kitsai is a Python package designed to streamline interactions with the Kits.AI API, offering convenient functionalities for voice models, voice conversions, vocal separations, and text-to-speech (TTS) tasks.

## Installation

Install kitsai via pip:

```bash
pip install kitsai

```

## Usage

### Authentication

To utilize any functions within this package, authentication via your API key is necessary. Simply invoke the `login` function from the `token` module, providing your API key as an argument.

```python
from kitsai import login

api_key = "YOUR_API_KEY_HERE"
login(api_key)
```

_You can generate an API key by signing up on the https://app.kits.ai/api-access website._

### Voice Models

#### Fetch Voice Models

Retrieve a list of available voice models.

```python
from kitsai import fetch_voice_models

voice_models = fetch_voice_models(order="asc", page=1, per_page=10, my_models=False, instruments=False)
```

#### Fetch Voice Model by ID

Fetch details of a specific voice model using its ID.

```python
from kitsai import fetch_voice_model_by_id

voice_model_id = 123
voice_model = fetch_voice_model_by_id(voice_model_id)
```

### Voice Conversions

#### Create Voice Conversion

Initiate a voice conversion task with specified parameters.

```python
from kitsai import create_voice_conversion

response = create_voice_conversion(
    voice_model_id=123,
    sound_file=open('input.wav', 'rb'),
    backing_sound_file=open('backing.wav', 'rb'),
    conversion_strength=0.5,
    model_volume_mix=0.8,
    pitch_shift=2,
    pre={
        "noiseGate": {
            "thresholdDb": -30,
            "ratio": 2,
            "attackMs": 10,
            "releaseMs": 20
        },
        "highPassFilter": {
            "cutoffFrequencyHz": 1000
        }
    }
)
```

#### Fetch Voice Conversion by ID

Retrieve details of a specific voice conversion task using its ID.

```python
from kitsai import fetch_voice_conversion_by_id

voice_conversion = fetch_voice_conversion_by_id("JOB_ID_HERE")
```

#### Fetch Voice Conversions

Retrieve a list of voice conversion tasks.

```python
from kitsai import fetch_voice_conversions

voice_conversions = fetch_voice_conversions(order="asc", page=1, per_page=10)
```

### Vocal Separations

#### Create Vocal Separation

Initiate a vocal separation task with an audio input.

```python
from kitsai import create_vocal_separation

response = create_vocal_separation(
    sound_file=open('input.wav', 'rb')
)
```

#### Fetch Vocal Separation by ID

Retrieve details of a specific vocal separation task using its ID.

```python
from kitsai import fetch_vocal_separation_by_id

vocal_separation = fetch_vocal_separation_by_id("JOB_ID_HERE")
```

#### Fetch Vocal Separations

Retrieve a list of vocal separation tasks.

```python
from kitsai import fetch_vocal_separations

vocal_separations = fetch_vocal_separations(order="asc", page=1, per_page=10)
```

### Text-to-Speech (TTS)

#### Create TTS

Generate text-to-speech output using a specified voice model and input text.

```python
from kitsai import create_tts

response = create_tts(
    voice_model_id=123,
    input_tts_text="Hello, how are you?"
)
```

#### Fetch TTS by ID

Retrieve details of a specific text-to-speech task using its ID.

```python
from kitsai import fetch_tts_by_id

tts_job = fetch_tts_by_id("JOB_ID_HERE")
```

#### Fetch TTS

Retrieve a list of text-to-speech tasks.

```python
from kitsai import fetch_tts

tts_jobs = fetch_tts(order="asc", page=1, per_page=10)
```

## License

This project is licensed under the Attribution-NonCommercial 4.0 International - see the [LICENSE](LICENSE) file for details.
