from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    RetrieveAPIView,
)

from . import models
from . import serializers


class CategoryView(RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = "name"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        if self.lookup_url_kwarg in self.request.GET:
            filter_kwargs = {
                self.lookup_url_kwarg: self.request.GET.get(self.lookup_url_kwarg)
            }
            obj = get_object_or_404(queryset, **filter_kwargs)
        else:
            obj = queryset.first()

        self.check_object_permissions(self.request, obj)

        return obj
