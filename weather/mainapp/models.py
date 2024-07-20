from django.db import models

class City(models.Model):
    name = models.CharField(max_length=60)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["-quantity"]
    
    def __str__(self):
        return self.name
# Create your models here.
