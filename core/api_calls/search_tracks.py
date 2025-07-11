import requests


def search_tracks(query, token):
    base_url = 'https://api.spotify.com/v1/search'
    params = {
        'q': query,
        'type': 'track',
        'limit': 10
    }
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['tracks']['items']

    return None
