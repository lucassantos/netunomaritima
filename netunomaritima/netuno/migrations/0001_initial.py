# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import netuno.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('link', models.CharField(max_length=1024)),
                ('imagem', models.CharField(max_length=1024)),
                ('upload', models.FileField(null=True, upload_to=netuno.models.anuncio_directory_path)),
                ('representante', models.CharField(max_length=512)),
                ('ativo', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Anuncios',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('legenda', models.CharField(max_length=512)),
                ('caminho', models.CharField(max_length=1024)),
                ('upload', models.FileField(null=True, upload_to=netuno.models.produtos_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('descricao', models.CharField(max_length=1024)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('senha', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=512)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netuno.Categoria')),
            ],
            options={
                'verbose_name_plural': 'SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=512)),
                ('bairro', models.CharField(max_length=512)),
                ('senha', models.CharField(max_length=256)),
                ('foto', models.CharField(max_length=1024)),
                ('upload', models.FileField(null=True, upload_to=netuno.models.usuario_directory_path)),
                ('cidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netuno.Cidade')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netuno.SubCategoria'),
        ),
        migrations.AddField(
            model_name='produto',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='netuno.Usuario'),
        ),
        migrations.AddField(
            model_name='foto',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='netuno.Produto'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netuno.Estado'),
        ),
    ]
