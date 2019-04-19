# Generated by Django 2.2 on 2019-04-19 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goodsapp', '0008_menumodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='parent_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent_menu_item', related_query_name='parent_menu_item', to='goodsapp.MenuModel'),
        ),
    ]