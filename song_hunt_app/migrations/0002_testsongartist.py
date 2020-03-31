# Generated by Django 2.2.6 on 2020-03-31 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song_hunt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSongArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artists', models.ManyToManyField(to='song_hunt_app.Artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song_hunt_app.Song', unique=True)),
            ],
        ),
    ]
