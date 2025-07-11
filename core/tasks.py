from celery import shared_task
from django.db import connection, transaction
from .models import HitSubmissions, CurrentHit


# remember to run
# celery -A hitlist worker --beat --loglevel=info
# after runserver in a new terminal


@shared_task()
def refresh_hit():
    with transaction.atomic():
        hit = HitSubmissions.objects.order_by('?').first()
        delete_tables()
        update_hit(hit)
        insert_default_data()


def delete_tables():
    tables = ['core_hitsubmissions', 'core_currenthit']
    for table in tables:
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {table} RESTART IDENTITY;')


def update_hit(hit):
    CurrentHit.objects.create(
        track_id=hit.track_id,
        track_name=hit.track_name,
        artist_name=hit.artist_name,
        image_link=hit.image_link
    )


def insert_default_data():
    HitSubmissions.objects.create(
        track_id='2Fxmhks0bxGSBdJ92vM42m',
        track_name='bad guy',
        artist_name='Billie Eilish',
        image_link='https://i.scdn.co/image/ab6761610000e5eb4a21b4760d2ecb7b0dcdc8da'
    )
