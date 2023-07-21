from django.db import models

# Create your models here.

STATUS = (
    ('yetkazib_berilgan','Yetkazib berilgan'),
    ('tayyorlanyapdi','Tayyorlanyapdi'),

)



class Dastavka(models.Model):
    """
    Dastavka uchun models
    """
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    count = models.PositiveBigIntegerField(default=1, null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    all_price = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS, default='tayyorlanyapdi')



    class Meta:
        ordering = ['id']
        verbose_name = 'Dastavka'
        verbose_name_plural = 'Dastavka'

    def __str__(self):
        return f"{self.full_name} {self.title}" 
        



    def product_price(self):
        return self.price * self.count    

        

