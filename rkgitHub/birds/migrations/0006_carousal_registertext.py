# Generated by Django 2.0.2 on 2018-04-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0005_auto_20180429_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousal',
            name='registerText',
            field=models.CharField(default='', max_length=50),
        ),
    ]