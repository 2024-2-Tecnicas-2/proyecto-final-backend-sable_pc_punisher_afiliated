# Generated by Django 5.1.2 on 2024-11-04 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_order_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoodieprintdesign',
            name='cantidad',
        ),
    ]
