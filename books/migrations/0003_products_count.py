# Generated by Django 3.2.8 on 2021-11-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20211103_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]