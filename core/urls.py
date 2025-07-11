from django.urls import path
from .views import IndexTemplateView, HitDayDetailView, SubmitAHitTemplateView, SearchListView, SuccessView, logout

app_name = "core"
urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("hit-of-the-day/", HitDayDetailView.as_view(), name="hit of the day"),
    path("submit-a-hit", SubmitAHitTemplateView.as_view(), name="submit a hit"),
    path("search/", SearchListView.as_view(), name="search"),
    path("success/", SuccessView.as_view(), name="success"),
    path("logout/", logout, name="logout")
]
