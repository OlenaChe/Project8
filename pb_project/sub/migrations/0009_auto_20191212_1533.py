# Generated by Django 2.2.7 on 2019-12-12 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0008_product_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='picture',
            new_name='img',
        ),
    ]