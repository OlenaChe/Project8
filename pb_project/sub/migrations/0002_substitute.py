# Generated by Django 2.2.7 on 2019-11-26 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('favorite_list', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub.Contact')),
                ('substitute_product', models.ManyToManyField(blank=True, related_name='products', to='sub.Product')),
                ('usual_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub.Product')),
            ],
        ),
    ]