from django.shortcuts import render
from django.db.models import Q
from .models import Categoria, Producto

def catalogo(request):
    query = request.GET.get('q')

    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(marca__icontains=query)
        ).prefetch_related('presentaciones', 'categoria')
    else:
        productos = Producto.objects.all().prefetch_related(
            'presentaciones', 'categoria'
        )

    categorias = Categoria.objects.all()

    pedido_confirmado = request.session.pop('pedido_confirmado', False)

    return render(request, 'catalogo/catalogo.html', {
        'categorias': categorias,
        'productos': productos,
        'query': query,
        'pedido_confirmado': pedido_confirmado
    })