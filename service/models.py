from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    contenied = models.CharField(max_length=50)
    image = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.title
