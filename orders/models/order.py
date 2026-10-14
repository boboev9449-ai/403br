
from django.db import models

class Order(models.Model):
    order = models.CharField("Заказ", max_length=100)
    customer = models.CharField("Клиент", max_length=100)
    orderdate = models.DateTimeField("Дата заказа")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.order
