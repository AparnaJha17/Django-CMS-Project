# Generated by Django 4.0.1 on 2022-08-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='project/static/assets/img'),
        ),
    ]