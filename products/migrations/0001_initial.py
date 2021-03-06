# Generated by Django 3.0.5 on 2020-09-15 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeMachineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeePodFlavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeePodPacksize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('dozen', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoffeePodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('display_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeePod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('flavor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.CoffeePodFlavor')),
                ('pack_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.CoffeePodPacksize')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.CoffeePodType')),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('water_line_compatible', models.BooleanField(default=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.CoffeeMachineModel')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.CoffeeMachineType')),
            ],
        ),
    ]
