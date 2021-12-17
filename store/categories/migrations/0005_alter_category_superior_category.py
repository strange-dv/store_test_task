# Generated by Django 3.2 on 2021-12-16 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_category_superior_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='superior_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinate_categories', to='categories.category'),
        ),
    ]