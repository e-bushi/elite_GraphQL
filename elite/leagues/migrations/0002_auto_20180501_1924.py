# Generated by Django 2.0.4 on 2018-05-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='league',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='squad',
        ),
        migrations.RemoveField(
            model_name='roster',
            name='player',
        ),
        migrations.RemoveField(
            model_name='roster',
            name='squad',
        ),
        migrations.RemoveField(
            model_name='league',
            name='teams',
        ),
        migrations.AlterField(
            model_name='league',
            name='league_description',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='season_dates',
            field=models.DateField(null=True),
        ),
        migrations.RemoveField(
            model_name='squad',
            name='players',
        ),
        migrations.AddField(
            model_name='squad',
            name='players',
            field=models.ManyToManyField(to='leagues.User'),
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Roster',
        ),
    ]
