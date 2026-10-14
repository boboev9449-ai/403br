from django.db import models

class Books(models.Model):
    Clientname = models.CharField("Название", max_length=100)
    addres = models.CharField("adres", max_length=100)
    Clientphone = models.IntegerField("Telefon")
    
    
    
    class Meta:
        verbose_name = "Kniga"
        verbose_name_plural = "Knigi"
        
        def __str__(self) -> str:
            return self.Clientname