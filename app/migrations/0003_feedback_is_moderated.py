# Generated by Django 3.2.7 on 2021-10-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211002_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_moderated',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
