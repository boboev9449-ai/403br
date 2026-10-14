
from django.db import models


class Item(models.Model):
    item = models.CharField("Предмет", max_length=100)
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
