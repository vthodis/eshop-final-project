# Generated by Django 2.2 on 2020-11-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_wishlist_wishlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(to='core.WishlistItem'),
        ),
    ]