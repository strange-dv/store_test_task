from django.db import models


class Category(models.Model):
    superior_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subordinate_categories",
        blank=True,
    )
    name = models.CharField(max_length=256, unique=True, db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
