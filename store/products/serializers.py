from rest_framework import serializers

from categories.serializers import SuperiorCategorySerializer
from . import models


class ProductSerializer(serializers.ModelSerializer):
    category = SuperiorCategorySerializer()

    class Meta:
        model = models.Product
        fields = ["name", "category"]
