# Generated by Django 4.0 on 2023-11-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_userpurchase_auditoryproductamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
