# Generated by Django 3.1.2 on 2020-10-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolao_app', '0004_bolao_esta_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apostador',
            name='credito',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bolao',
            name='esta_ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bolao',
            name='premiacao',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bolao',
            name='valor_disputado',
            field=models.FloatField(default=0.0),
        ),
    ]
