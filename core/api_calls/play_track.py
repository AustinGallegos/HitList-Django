import requests


def play_track(track_id, device_id, token):
    url = 'https://api.spotify.com/v1/me/player/play'
    params = {
        'device_id': device_id
    }
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    json = {
        'uris': [f'spotify:track:{track_id}']
    }

    response = requests.put(url, params=params, headers=headers, json=json)
    if response.status_code == 204:
        print('Track playing')
    else:
        print('Track failed to play')
        print(response.json())
