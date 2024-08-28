import uuid
from django.db import models

class Category(models.Model):
    code = models.UUIDField("Código uuid4", default=uuid.uuid4, editable=False)
    name = models.CharField('Name', max_length=255)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
