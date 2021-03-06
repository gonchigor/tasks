# Generated by Django 2.2 on 2019-04-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dimensionsapp', '0007_auto_20190408_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agerestriction',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='binding',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='formatbook',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='jenre',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='publishinghouse',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
    ]
