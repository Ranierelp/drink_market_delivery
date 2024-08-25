from django.db import models
from user.models import CustomUser
from category.models import Category
class Product(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.TextField('Description', null=True, blank=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Quantity')
    photo = models.ImageField('Photo', upload_to='products_img', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name
class order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
    def __str__(self):
        return f'{self.user.name} - {self.total}'
    
class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    