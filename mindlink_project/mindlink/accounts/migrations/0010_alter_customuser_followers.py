# Generated by Django 4.2.7 on 2023-12-12 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_relations', '0002_remove_relations_follower_remove_relations_following_and_more'),
        ('accounts', '0009_alter_customuser_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(related_name='following_users', through='user_relations.Relations', to=settings.AUTH_USER_MODEL),
        ),
    ]
