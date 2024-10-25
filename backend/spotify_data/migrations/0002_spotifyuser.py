# Generated by Django 4.1 on 2024-10-25 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotify_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile_image_url', models.URLField(blank=True, null=True)),
                ('favorite_tracks_short', models.JSONField(blank=True, null=True)),
                ('favorite_tracks_medium', models.JSONField(blank=True, null=True)),
                ('favorite_tracks_long', models.JSONField(blank=True, null=True)),
                ('favorite_artists_short', models.JSONField(blank=True, null=True)),
                ('favorite_artists_medium', models.JSONField(blank=True, null=True)),
                ('favorite_artists_long', models.JSONField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
