# Generated by Django 2.1.2 on 2018-10-20 01:14

from django.db import migrations

def add_groups(apps, schema_editor):
    #friends
    friends, created = Group.objects.get_or_create(name='friends')   
    if created:
        logger.info('friends Group created')

    #couple
    couple, created = Group.objects.get_or_create(name='couple')   
    if created:
        group.permissions.add('gallery.approve_photo')
        logger.info('couple Group created')

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
    ]
