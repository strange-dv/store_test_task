from rest_framework import serializers

from . import models


class SuperiorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    superior_category = SuperiorCategorySerializer()

    class Meta:
        model = models.Category
        fields = [
            "name",
            "subordinate_categories",
            "superior_category",
        ]
        read_only_fields = [
            "subordinate_categories",
            "superior_category",
        ]

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields["subordinate_categories"] = CategorySerializer(many=True)
        return fields
