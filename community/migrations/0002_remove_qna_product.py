# Generated by Django 3.2.13 on 2022-11-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qna',
            name='Product',
        ),
    ]