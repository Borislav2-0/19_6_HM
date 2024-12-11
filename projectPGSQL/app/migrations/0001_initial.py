# Generated by Django 5.1.4 on 2024-12-11 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Ceramics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название товара')),
                ('short_descr', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('material', models.CharField(max_length=100, verbose_name='Материал')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Керамическое изделие',
                'verbose_name_plural': 'Керамические изделия',
            },
        ),
        migrations.CreateModel(
            name='Joinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название товара')),
                ('short_descr', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('material', models.CharField(max_length=100, verbose_name='Материал')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Стоимость')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Столярное изделие',
                'verbose_name_plural': 'Столярные изделия',
            },
        ),
    ]
