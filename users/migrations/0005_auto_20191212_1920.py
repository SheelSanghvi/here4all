# Generated by Django 2.2.7 on 2019-12-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191212_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/profile_photo'),
        ),
    ]
