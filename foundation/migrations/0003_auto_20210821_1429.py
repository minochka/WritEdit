# Generated by Django 3.2.6 on 2021-08-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0002_alter_userprofile_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статус'),
        ),
    ]