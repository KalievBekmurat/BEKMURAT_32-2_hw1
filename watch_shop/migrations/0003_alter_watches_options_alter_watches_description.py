# Generated by Django 4.2.5 on 2023-09-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_shop', '0002_alter_watches_characteristics_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watches',
            options={'verbose_name': 'Новинку', 'verbose_name_plural': 'Новинки'},
        ),
        migrations.AlterField(
            model_name='watches',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Укажите описание часов'),
        ),
    ]