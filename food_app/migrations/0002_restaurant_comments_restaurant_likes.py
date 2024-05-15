# Generated by Django 5.0.4 on 2024-05-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
        ('likeNcom_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='comments',
            field=models.ManyToManyField(to='likeNcom_app.comment'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='likes',
            field=models.ManyToManyField(to='likeNcom_app.like'),
        ),
    ]