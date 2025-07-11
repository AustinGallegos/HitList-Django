import requests


def get_subscription(token):
    url = 'https://api.spotify.com/v1/me'
    headers = get_headers(token)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['product']
    else:
        return None


def get_headers(token):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    return headers
