# Generated by Django 3.1.1 on 2020-09-26 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0002_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
