# Generated by Django 2.2.7 on 2019-12-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0009_auto_20191212_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutrition',
            field=models.TextField(default='X'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.TextField(default='X'),
        ),
    ]
