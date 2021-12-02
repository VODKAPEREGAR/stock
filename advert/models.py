import os.path
from django.db import models
import uuid


class Category(models.Model):
    category_id = (
        models.AutoField(
            primary_key=True
        )
    )

    category_name = (
        models.CharField(
            max_length=65,
            verbose_name="Название категории"
        )
    )

    slug = (
        models.SlugField(
            max_length=64
        )
    )

    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    subcategory_id = (
        models.AutoField(
            primary_key=True
        )
    )

    subcategory_name = (
        models.CharField(
            max_length=65,
            verbose_name="Название субкатегории"
        )
    )

    category = (
        models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            null=True
        )
    )

    slug = (
        models.SlugField(
            max_length=64
        )
    )

    def __str__(self):
        return self.subcategory_name


class City(models.Model):
    city_id = (
        models.AutoField(
            primary_key=True
        )
    )

    city_name = (
        models.CharField(
            max_length=65,
            verbose_name="Название города"
        )
    )

    slug = (
        models.SlugField(
            max_length=64
        )
    )

    def __str__(self):
        return self.city_name


class Advert(models.Model):
    id = (
        models.AutoField(
            primary_key=True
        )
    )

    category = (
        models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            null=True
        )
    )

    subcategory = (
        models.ForeignKey(
            Subcategory,
            on_delete=models.CASCADE,
            null=True
        )
    )

    title = (
        models.CharField(
            max_length=65,
            verbose_name="Название объявления"
        )
    )

    city = (
        models.ForeignKey(
            City,
            on_delete=models.CASCADE,
            null=True
        )
    )

    price = (
        models.DecimalField(
            max_digits=8,
            decimal_places=2,
            verbose_name="Цена"
        )
    )

    description = (
        models.TextField(
            max_length=256,
            verbose_name="Описание",
            blank=True
        )
    )

    status = (
        models.CharField(
            choices=[
                ('active', 'Активные'),
                ('moderation', 'На модерации'),
                ('rejected', 'Отклоненные'),
                ('inactive', 'Неактивные'),
            ],
            default=('moderation'),
            max_length=12
        )
    )

    slug = (
        models.SlugField(
            max_length=64
        )
    )
    

    def __str__(self):
        return self.title


