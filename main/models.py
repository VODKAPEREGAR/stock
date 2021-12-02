from django.db import models


class Help(models.Model):
    id = (
        models.AutoField(
            primary_key=True
        )
    )


    title = (
        models.CharField(
            max_length=65,
            verbose_name="Тема",
            blank=False,
            null=False
        )
    )


    description = (
        models.TextField(
            max_length=256,
            verbose_name="Описание",
            blank=False,
            null=False
        )
    )

    emanil = (
        models.EmailField(
            max_length=65,
            verbose_name="Email для свзяи",
            blank=False,
            null=False
        )
    )

    def __str__(self):
        return self.title
