# Generated by Django 5.0.7 on 2024-08-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publication', '0002_contactformsubmission_postformsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformsubmission',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
