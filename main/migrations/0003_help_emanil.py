# Generated by Django 3.2.9 on 2021-12-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_advert_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='emanil',
            field=models.CharField(default=1, max_length=65, verbose_name='Email для свзяи'),
            preserve_default=False,
        ),
    ]