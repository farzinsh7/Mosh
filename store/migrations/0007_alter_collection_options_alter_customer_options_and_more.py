# Generated by Django 4.1.5 on 2023-01-31 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_cat_cartitem_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
    ]
