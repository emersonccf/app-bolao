# Generated by Django 3.1.2 on 2020-10-25 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_app', '0003_auto_20201024_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolao',
            name='esta_ativo',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]