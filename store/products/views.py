from rest_framework.generics import (
    ListAPIView,
)

from . import models
from . import serializers


class ListProductView(ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def filter_queryset(self, queryset):
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category__name=category)

        return queryset
