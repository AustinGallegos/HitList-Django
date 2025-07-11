import json
from django.test import TestCase
from django.urls import reverse
from .models import HitSubmissions, CurrentHit
from .tasks import refresh_hit


class HitSubmissionsModelTests(TestCase):
    def test_is_invalid(self):
        hit = HitSubmissions(track_id="1234567890123456789012")
        self.assertIs(all([hit.track_id, hit.track_name, hit.artist_name, hit.image_link]), False)


class HitDayDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        CurrentHit.objects.create(
            track_id="3ZFTkvIE7kyPt6Nu3PEa7V",
            track_name="Hips Don't Lie (feat. Wyclef Jean)",
            artist_name="Shakira",
            image_link="https://i.scdn.co/image/ab67616d0000b27327ddd747545c0d0cfe7595fa"
        )

        HitSubmissions.objects.create(
            track_id="2Fxmhks0bxGSBdJ92vM42m",
            track_name="bad guy",
            artist_name="Billie Eilish",
            image_link="https://i.scdn.co/image/ab6761610000e5eb4a21b4760d2ecb7b0dcdc8da"
        )

    def test_hit_showing(self):
        url = reverse("core:hit of the day")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["hit"].track_name, "Hips Don't Lie (feat. Wyclef Jean)")

    def test_refresh_hit(self):
        refresh_hit()
        url = reverse("core:hit of the day")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["hit"].track_name, "bad guy")


class SuccessViewTest(TestCase):
    def test_submit_hit(self):
        url = reverse("core:success")
        data = {
            "trackID": "2Fxmhks0bxGSBdJ92vM42m",
            "trackName": "bad guy",
            "artist": "Billie Eilish",
            "image": "https://i.scdn.co/image/ab6761610000e5eb4a21b4760d2ecb7b0dcdc8da"
        }

        response = self.client.post(url, data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        hit = HitSubmissions.objects.first()
        self.assertEqual(hit.artist_name, "Billie Eilish")
        self.assertEqual(hit.track_name, "bad guy")
