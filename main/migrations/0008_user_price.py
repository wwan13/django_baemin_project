# Generated by Django 3.1 on 2020-08-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200809_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
