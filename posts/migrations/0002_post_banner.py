# Generated by Django 5.0.2 on 2025-06-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank='True', default='1.png', upload_to=''),
        ),
    ]
