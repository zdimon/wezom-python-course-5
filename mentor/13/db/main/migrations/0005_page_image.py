# Generated by Django 3.2 on 2021-04-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210424_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='pages', verbose_name='Image', width_field=300),
        ),
    ]
