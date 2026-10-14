
from django.db import models


class Customers(models.Model):
    customer = models.CharField("Клиент", max_length=100)
    country = models.CharField("Страна", max_length=100)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.customer
