import requests
from .play_track import play_track


def get_device(track_id, token):
    url = 'https://api.spotify.com/v1/me/player/devices'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        if len(data['devices']) > 0:
            device_id = data['devices'][0]['id']
            device_name = data['devices'][0]['name']
            play_track(track_id, device_id, token)

            return device_name

        else:
            return None
