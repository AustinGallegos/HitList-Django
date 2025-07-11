import json
from django.views.generic import DetailView, TemplateView, ListView, View
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.middleware.csrf import get_token
from django.urls import reverse
from urllib.parse import urlencode
from .models import CurrentHit, HitSubmissions
import core.handlers as handlers


class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code', '')
        if code:
            base_url = reverse('core:hit of the day')
            query_string = urlencode({'code': code})
            url = f'{base_url}?{query_string}'
            return redirect(url)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = handlers.index(self.request)

        for key, val in data.items():
            context[key] = val

        return context


class HitDayDetailView(DetailView):
    template_name = "core/hit_day.html"
    context_object_name = "hit"

    def get_object(self, queryset=None):
        return get_object_or_404(CurrentHit, pk=1)

    def get(self, request, *args, **kwargs):
        error = request.GET.get('error')
        if error:
            return redirect(reverse("core:index"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = handlers.hit_day(self.request, self.object.track_id)

        for key, val in data.items():
            context[key] = val

        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)

        access_token = context.get('access_token')
        if access_token:
            response.set_cookie('access_token', context['access_token'], max_age=3600)

        subscription = context.get('subscription')
        if subscription:
            response.set_cookie('subscription', context['subscription'], max_age=3600)

        return response


class SubmitAHitTemplateView(TemplateView):
    template_name = "core/submit_a_hit.html"


class SearchListView(ListView):
    template_name = "core/search.html"
    context_object_name = "tracks"

    def get_queryset(self):
        if hasattr(self, '_cached_queryset'):
            return self._cached_queryset

        qs = handlers.search(self.request)
        self._cached_queryset = qs
        return qs

    def get(self, request, *args, **kwargs):
        get_token(request)
        queryset = self.get_queryset()
        if not queryset:
            return redirect(reverse("core:index"))

        self.object_list = queryset
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        subscription = self.request.COOKIES.get('subscription')
        context['is_premium'] = subscription
        return context


class SuccessView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        track_id = data.get('trackID')
        track_name = data.get('trackName')
        artist_name = data.get('artist')
        image_link = data.get('image')

        track = HitSubmissions.objects.create(
            track_id=track_id,
            track_name=track_name,
            artist_name=artist_name,
            image_link=image_link
        )

        context = {
            'track_name': track_name,
            'artist_name': artist_name,
            'image_link': image_link
        }

        return render(request, 'core/success.html', context)

    def get(self, request, *args, **kwargs):
        return redirect(reverse("core:index"))


def logout(request):
    response = HttpResponse('Successfully logged out.')
    cookies = ['subscription', 'access_token']
    for cookie in cookies:
        response.delete_cookie(cookie)
    return response
