# Generated by Django 4.2.7 on 2023-11-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBamp', '0002_categoriarestaurante_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriarestaurante',
            name='imagen',
            field=models.ImageField(upload_to=None),
        ),
    ]