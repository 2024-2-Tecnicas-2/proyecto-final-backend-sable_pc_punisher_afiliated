# Generated by Django 5.1.2 on 2024-11-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_printdesign_picturesize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoodie',
            name='hood',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hoodie',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hoodie',
            name='print',
            field=models.BooleanField(default=False),
        ),
    ]