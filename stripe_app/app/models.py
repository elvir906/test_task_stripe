from django.db import models


class Item (models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name

    def to_monetary_value(self):
        return f"{self.price:.2f}"

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
