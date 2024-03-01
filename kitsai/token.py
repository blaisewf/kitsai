class TokenError(Exception):
    pass

_api_key = None

def login(api_key):
    global _api_key
    if not api_key:
        raise TokenError("API key is empty. Please provide a valid API key.")
    _api_key = api_key

def get_api_key():
    if not _api_key:
        raise TokenError("API key not set. Please call login() first.")
    return _api_key
