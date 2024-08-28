import uuid
from django.db import models
from user.models import CustomUser

class Address(models.Model):
    code = models.UUIDField("Código uuid4", default=uuid.uuid4, editable=False)
    street = models.CharField('Street', max_length=255)
    number = models.CharField('Number', max_length=10)
    complement = models.CharField('Complement', max_length=255, null=True, blank=True)
    neighborhood = models.CharField('Neighborhood', max_length=255)
    city = models.CharField('City', max_length=255)
    state = models.CharField('State', max_length=2)
    country = models.CharField('Country', max_length=255)
    zip_code = models.CharField('Zip Code', max_length=9)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        
    def __str__(self):
        return f'{self.street}, {self.number}, {self.city}/{self.state}'
    
