# Generated by Django 5.0.7 on 2024-08-02 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_publication', models.DateTimeField()),
                ('pub_text', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Author.author')),
            ],
            options={
                'db_table': 'publications',
            },
        ),
    ]
