# Generated by Django 2.2.10 on 2020-03-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0005_auto_20200303_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]