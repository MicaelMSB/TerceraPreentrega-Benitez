# Generated by Django 4.2.4 on 2023-09-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBar', '0003_cliente_email_alter_cliente_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
