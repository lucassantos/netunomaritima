 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

def usuario_directory_path(instance, filename):
   return 'media/usuario/{0}_{1}'.format(instance.id, instance.nome)

def anuncio_directory_path(instance, filename):
   return 'media/anuncios/{0}_{1}'.format(instance.id, instance.titulo)

def produtos_directory_path(instance, filename):
   return 'media/produtos/{0}_{1}'.format(instance.produto.id, instance.id)

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    class Meta:
        verbose_name_plural = "Estados"
    def __unicode__(self):
        return str(self.nome)

class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    estado = models.ForeignKey(Estado, null=True)
    class Meta:
        verbose_name_plural = "Cidades"
    def __unicode__(self):
        return str(self.nome)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    class Meta:
        verbose_name_plural = "Categorias"
    def __unicode__(self):
        return str(self.titulo)

class SubCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    categoria = models.ForeignKey(Categoria, null=True)
    class Meta:
        verbose_name_plural = "SubCategorias"
    def __unicode__(self):
        return str(self.titulo)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    email = models.EmailField(max_length=512)
    cidade = models.ForeignKey(Cidade, null=True)
    bairro = models.CharField(max_length=512)
    senha = models.CharField(max_length=256)
    foto = models.CharField(max_length=1024)
    upload = models.FileField(upload_to=usuario_directory_path, null=True)
    class Meta:
        verbose_name_plural = "Usuarios"
    def __unicode__(self):
        return str(self.nome)

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    descricao = models.CharField(max_length=1024)
    subcategoria = models.ForeignKey(SubCategoria, null=True)
    preco = models.DecimalField(default=0, decimal_places=2, max_digits=14)
    senha = models.CharField(max_length=256)
    usuario = models.ForeignKey(Usuario, null=True, related_name="produtos")
    class Meta:
        verbose_name_plural = "Produtos"
    def __unicode__(self):
        return str(self.nome)

class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    legenda = models.CharField(max_length=512)
    caminho = models.CharField(max_length=1024)
    upload = models.FileField(upload_to=produtos_directory_path, null=True)
    produto = models.ForeignKey(Produto, null=True, related_name="fotos")
    class Meta:
        verbose_name_plural = "Fotos"
    def __unicode__(self):
        return str(self.legenda)

class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=512)
    link = models.CharField(max_length=1024)
    imagem = models.CharField(max_length=1024)
    upload = models.FileField(upload_to=anuncio_directory_path, null=True)
    representante = models.CharField(max_length=512)
    ativo = models.BooleanField(default=True)
    email = models.CharField(max_length=512)
    class Meta:
        verbose_name_plural = "Anuncios"
    def __unicode__(self):
        return str(self.titulo)
