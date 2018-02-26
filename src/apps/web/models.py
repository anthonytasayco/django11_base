from django.db import models

# Create your models here.


class Producto(models.Model):
    name = models.CharField('Name', max_length=255, blank=True)
    description = models.TextField('Description', blank=True)
    featured = models.BooleanField('Featured', default=False)
    offer = models.BooleanField('Offer', default=False)
    price = models.DecimalField('Price', max_digits=12,
                                decimal_places=2, default=0)

    class Meta:
        verbose_name = u'Product'
        verbose_name_plural = u'Products'
