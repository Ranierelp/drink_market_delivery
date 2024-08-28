from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModeelSerializer):
    class Meta:
        model = Category
        fields = '__all__'