# Generated by Django 3.2.9 on 2021-11-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0003_rename_name_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]