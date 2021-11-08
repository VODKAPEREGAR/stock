# Generated by Django 3.2.9 on 2021-11-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_alter_advert_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='status',
            field=models.CharField(choices=[('active', 'Активные'), ('moderation', 'На модерации'), ('rejected', 'Отклоненные'), ('inactive', 'Неактивные')], default=('moderation', 'На модерации'), max_length=12),
        ),
    ]