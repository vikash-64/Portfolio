# Generated by Django 4.0.3 on 2022-03-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devFolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ProjectLink',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
