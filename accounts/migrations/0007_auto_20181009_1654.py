# Generated by Django 2.0.7 on 2018-10-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181009_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claimdata',
            old_name='Location',
            new_name='ActualLocation',
        ),
        migrations.AddField(
            model_name='claimdata',
            name='LocationEntered',
            field=models.CharField(default='', max_length=100),
        ),
    ]