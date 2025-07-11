import requests


def get_track_data(id, token):
    url = f'https://api.spotify.com/v1/tracks/{id}'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None
