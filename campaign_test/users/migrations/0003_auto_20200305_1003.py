# Generated by Django 3.0.2 on 2020-03-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='uuid',
        ),
        migrations.AddField(
            model_name='user',
            name='cities',
            field=models.ManyToManyField(to='campaigns.City'),
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(to='campaigns.Language'),
        ),
    ]