# Generated by Django 4.0.4 on 2022-05-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadID', '0003_id_item_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id_item',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
