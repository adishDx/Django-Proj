# Generated by Django 2.0.2 on 2018-04-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0010_auto_20180430_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='fame',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('EEE', 'EEE'), ('MBA', 'MBA'), ('MCA', 'MCA'), ('B.Pharma', 'B.Pharma')], default='CSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='core',
            name='year',
            field=models.CharField(choices=[('First Year', 'I'), ('Second Year', 'II'), ('Third Year', 'III'), ('Fourth Year', 'IV')], default='', max_length=15),
        ),
    ]
