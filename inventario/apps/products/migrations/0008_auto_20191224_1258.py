# Generated by Django 2.2.8 on 2019-12-24 15:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_warehouse_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='warehouses',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descriptionWarehouse', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('MinimumStock', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='warehouseProduct',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.warehouses'),
        ),
        migrations.DeleteModel(
            name='warehouse',
        ),
    ]