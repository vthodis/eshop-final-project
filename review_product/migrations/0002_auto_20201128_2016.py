# Generated by Django 2.2 on 2020-11-28 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_delete_review'),
        ('review_product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviewed',
            new_name='ReviewItem',
        ),
    ]
