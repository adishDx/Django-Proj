# Generated by Django 2.0.2 on 2018-04-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0009_core_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='year',
            field=models.CharField(choices=[('I', 'First'), ('II', 'Second')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='core',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('ME', 'ME'), ('EEE', 'EEE'), ('MBA', 'MBA'), ('MCA', 'MCA'), ('B.Pharma', 'B.Pharma')], default='CSE', max_length=10),
        ),
    ]
