# Generated by Django 3.1.5 on 2021-11-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_products_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]