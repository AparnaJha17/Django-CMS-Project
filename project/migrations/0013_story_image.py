# Generated by Django 4.0.1 on 2022-09-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
