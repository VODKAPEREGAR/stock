# Generated by Django 3.2.9 on 2021-11-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_auto_20211108_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(blank=True, max_length=256, verbose_name='Описание'),
        ),
    ]