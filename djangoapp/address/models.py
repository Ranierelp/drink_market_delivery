from django.db import models
from user.models import CustomUser

class Address(models.Model):
    street = models.CharField('Street', max_length=255)
    number = models.CharField('Number', max_length=10)
    complement = models.CharField('Complement', max_length=255, null=True, blank=True)
    neighborhood = models.CharField('Neighborhood', max_length=255)
    city = models.CharField('City', max_length=255)
    state = models.CharField('State', max_length=2)
    country = models.CharField('Country', max_length=255)
    zip_code = models.CharField('Zip Code', max_length=9)
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        
    def __str__(self):
        return f'{self.street}, {self.number}, {self.city}/{self.state}'
    
class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'address')  # Garante que não haja duplicatas

    def __str__(self):
        return f'{self.user.name} - {self.address}'
