import core.api_calls as api_calls


def search(request):
    token = request.COOKIES.get('access_token')
    if not token:
        return None

    is_premium = request.COOKIES.get('subscription')
    if not is_premium:
        return ['not premium']

    query = request.GET.get('query')
    tracks = api_calls.search_tracks(query, token)

    res = []
    parse_tracks(tracks, token, res)

    return res


def parse_tracks(tracks, token, res):
    for track in tracks:
        track_data = api_calls.get_track_data(track['id'], token)
        track_info = {
            'track_id': track['id'],
            'artist_name': track_data['artists'][0]['name'],
            'track_name': track_data['name'],
            'image_link': track_data['album']['images'][0]['url']
        }
        res.append(track_info)
