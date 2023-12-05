# Generated by Django 5.0 on 2023-12-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='implementosdeportivos',
            name='precio',
        ),
        migrations.AlterField(
            model_name='ropa',
            name='talla',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('X', 'X'), ('XL', 'XL')], help_text='Seleccione  una talla', max_length=4),
        ),
    ]