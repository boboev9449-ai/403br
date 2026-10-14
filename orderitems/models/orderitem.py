
from django.db import models


class OrderItem(models.Model):
    orderitem = models.CharField("Позиция заказа", max_length=100)
    order = models.CharField("Заказ", max_length=100)
    item = models.CharField("Товар", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.IntegerField("Количество")

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return self.orderitem
