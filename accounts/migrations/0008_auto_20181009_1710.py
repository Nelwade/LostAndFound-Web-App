# Generated by Django 2.0.7 on 2018-10-09 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20181009_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claimdata',
            old_name='ActualLocation',
            new_name='Location',
        ),
        migrations.RemoveField(
            model_name='claimdata',
            name='LocationEntered',
        ),
    ]