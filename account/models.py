from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

city_list = (
    ('minsk', 'Минск'),
    ('brest', 'Брест'),
)

gender_list = (
    ('not_selected', 'Не выбран'),
    ('man', 'Мужской'),
    ('woman', 'Женский'),
)


class Profile(AbstractUser):
    city = (
        models.CharField(
            max_length=8,
            choices=city_list,
            verbose_name='Город'
        )
    )

    gender = (
        models.CharField(
            max_length=12,
            choices=gender_list
        )
    )

    # phone = (
    #     PhoneNumberField(
    #         max_length=13,
    #         unique = True,
    #         null = False,
    #         blank = False
    #     )
    # )
