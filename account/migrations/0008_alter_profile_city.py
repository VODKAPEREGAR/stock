# Generated by Django 3.2.9 on 2021-12-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('minsk', 'Минск'), ('brest', 'Брест')], max_length=8, verbose_name='Город'),
        ),
    ]