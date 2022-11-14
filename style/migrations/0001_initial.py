# Generated by Django 3.2.13 on 2022-11-14 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[('캐주얼룩', '캐주얼룩'), ('데이트룩', '데이트룩'), ('포멀룩', '포멀룩'), ('스트릿룩', '스트릿룩'), ('걸리쉬룩', '걸리쉬룩')], max_length=23)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
