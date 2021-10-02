# Generated by Django 3.2.7 on 2021-10-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/app_pics/imageNotAvailable_grid.png', null=True, upload_to='user_avatars'),
        ),
    ]
