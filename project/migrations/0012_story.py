# Generated by Django 4.0.1 on 2022-09-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='#', max_length=300)),
                ('name', models.CharField(default='#', max_length=100)),
                ('place', models.CharField(default='#', max_length=200)),
            ],
        ),
    ]