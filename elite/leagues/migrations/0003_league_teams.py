# Generated by Django 2.0.4 on 2018-05-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20180501_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='teams',
            field=models.ManyToManyField(to='leagues.Squad'),
        ),
    ]