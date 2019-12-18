# Generated by Django 2.2.7 on 2019-12-18 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0010_auto_20191217_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub.Contact')),
                ('favorite', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_product', to='sub.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Substitute',
        ),
    ]