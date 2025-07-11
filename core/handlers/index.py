import os
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()


def index(request):
    context = dict()

    has_token = access_token(request)
    if has_token:
        context['access_token'] = True
    else:
        context['access_token'] = False
        redirect_url = get_spotify_redirect()
        context['redirect_url'] = redirect_url

    return context


def access_token(request):
    if 'access_token' in request.COOKIES:
        return True
    return False


def get_spotify_redirect():
    base_url = 'https://accounts.spotify.com/authorize'
    params = build_params()
    final_url = f'{base_url}?{urlencode(params)}'

    return final_url


def build_params():
    params = {
        'client_id': os.getenv('CLIENT_ID'),
        'response_type': 'code',
        'redirect_uri': 'http://127.0.0.1:8000/',
        'scope': 'user-read-playback-state user-modify-playback-state user-read-private'
    }

    return params

