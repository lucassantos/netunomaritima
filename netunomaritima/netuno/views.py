from django.shortcuts import render, redirect, render_to_response
from django.http.response import HttpResponse
from netuno.models import *
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.template import RequestContext
import json

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def sobre(request):
    context = {}
    return render(request, 'sobre.html', context)

def produtos(request):
    # Filtros
    id = request.GET.get("id")
    produto = request.GET.get("produto")
    descricao = request.GET.get("descricao")
    subcategoria_id = request.GET.get("subcategoria_id")
    preco_min = request.GET.get("preco_min")
    preco_max = request.GET.get("preco_max")
    usuario_id = request.GET.get("usuario_id")

    query = Produto.objects.all()

    if(id):
        query = query.filter(id=id)
    else:
        if(produto):
            query = query.filter(titulo__icontains=produto)
        if(descricao):
            query = query.filter(descricao__icontains=descricao)
        if(subcategoria_id):
            query = query.filter(subcategoria__id=subcategoria__id)
        if(preco_min):
            query = query.filter(preco__gte=preco_min)
        if(preco_max):
            query = query.filter(preco__lte=preco_max)
        if(usuario_id):
            query = query.filter(usuario__id=usuario__id)


    lista = serialize('json', query, fields=["titulo", "descricao", "subcategoria", "preco", "usuario"])

    return HttpResponse(lista, content_type='application/json')

def usuarios(request):
    # Filtros
    id = request.GET.get("id")
    nome = request.GET.get("nome")
    email = request.GET.get("email")
    cidade_id = request.GET.get("cidade_id")
    bairro = request.GET.get("bairro")

    query = Usuario.objects.all()

    if(id):
        query = query.filter(id=id)
    else:
        if(nome):
            query = query.filter(nome__icontains=nome)
        if(email):
            query=query.filter(email__icontains=email)
        if(cidade_id):
            query=query.filter(cidade__id=cidade__id)
        if(bairro):
            query=query.filter(bairro__icontains=bairro)



    lista = serialize('json', query, fields=["nome", "email", "cidade", "bairro", "upload"])

    return HttpResponse(lista, content_type='application/json')
