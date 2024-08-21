# Generated by Django 5.0.7 on 2024-08-20 01:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_contactform_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='ingredients',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flan',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flan',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
