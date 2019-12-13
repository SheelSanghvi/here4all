# Generated by Django 2.2.7 on 2019-12-13 14:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191213_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='favourited_by',
            field=models.ManyToManyField(related_name='favourited_blogs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='additional_data',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]
