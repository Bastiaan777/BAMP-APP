# Generated by Django 4.2.7 on 2023-12-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBamp', '0004_perfilusuario_alter_pedido_usuario_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='fechaNacimiento',
            field=models.DateTimeField(blank=True),
        ),
    ]