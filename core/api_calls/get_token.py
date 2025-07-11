import os
from dotenv import load_dotenv
import requests
import base64

load_dotenv()


def get_token(request):
    url = 'https://accounts.spotify.com/api/token'
    body, headers = get_body_headers(request)
    response = requests.post(url, data=body, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['access_token']
    else:
        return None


def get_body_headers(request):
    body = build_body(request)
    headers = build_headers()

    return body, headers


def build_body(request):
    body = {
        'grant_type': 'authorization_code',
        'code': request.GET.get('code', ''),
        'redirect_uri': 'http://127.0.0.1:8000/',
    }

    return body


def build_headers():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    auth_str = f'{client_id}:{client_secret}'
    auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        'Authorization': f'Basic {auth_str}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    return headers
