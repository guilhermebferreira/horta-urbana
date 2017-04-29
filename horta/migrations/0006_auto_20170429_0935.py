# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horta', '0005_auto_20170429_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ('nome',), 'verbose_name': 'Cliente', 'verbose_name_plural': 'Cliente'},
        ),
        migrations.AlterModelOptions(
            name='feirante',
            options={'ordering': ('nome', 'organico'), 'verbose_name': 'Feirante', 'verbose_name_plural': 'Feirantes'},
        ),
        migrations.AlterModelOptions(
            name='pacote',
            options={'ordering': ('nome', 'organico'), 'verbose_name': 'Pacote', 'verbose_name_plural': 'Pacote'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ('data', 'cliente'), 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AddField(
            model_name='pagamento',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horta.Cliente'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='horta.Pagamento'),
        ),
    ]
