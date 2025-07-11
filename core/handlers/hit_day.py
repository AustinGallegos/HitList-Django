import core.api_calls as api_calls


def hit_day(request, track_id):
    context = dict()
    token = get_access_token(request, context)
    is_premium = get_subscription(request, token, context)
    device = api_calls.get_device(track_id, token)

    context['is_premium'] = is_premium
    context['device_name'] = device

    return context


def get_access_token(request, context):
    token = request.COOKIES.get('access_token')
    if not token:
        token = api_calls.get_token(request)
        context['access_token'] = token

    return token


def get_subscription(request, token, context):
    subscription = request.COOKIES.get('subscription')
    if not subscription:
        subscription = api_calls.get_subscription(token)
        context['subscription'] = subscription

    return subscription == 'premium'
