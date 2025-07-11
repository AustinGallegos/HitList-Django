from django.contrib import admin
from .models import HitSubmissions, CurrentHit


@admin.register(HitSubmissions)
class HitSubmissionsAdmin(admin.ModelAdmin):
    list_display = ["track_name", "artist_name", "image_link", "track_id"]
    search_fields = ["track_name", "artist_name"]


@admin.register(CurrentHit)
class CurrentHitAdmin(admin.ModelAdmin):
    list_display = ["track_name", "artist_name", "image_link", "track_id"]
