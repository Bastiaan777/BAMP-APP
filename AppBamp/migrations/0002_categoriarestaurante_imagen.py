# Generated by Django 4.2.7 on 2023-11-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBamp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriarestaurante',
            name='imagen',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
