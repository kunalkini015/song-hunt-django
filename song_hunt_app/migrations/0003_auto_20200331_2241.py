# Generated by Django 2.2.6 on 2020-03-31 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song_hunt_app', '0002_testsongartist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsongartist',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song_hunt_app.Song'),
        ),
    ]
