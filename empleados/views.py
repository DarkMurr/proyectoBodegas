from bodegas.utils import descontar_stock
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from bodegas.models import Inventario
from pedidos.models import Pedido
from catalogo.models import Presentacion
from pedidos.models import Pedido, DetallePedido

@login_required
def dashboard(request):
    return render(request, 'empleados/dashboard.html')

@login_required
def inventario(request):
    inventarios = Inventario.objects.select_related(
        'presentacion',
        'presentacion__producto',
        'bodega'
    )
    return render(request, 'empleados/inventario.html', {'inventarios': inventarios})

@login_required
def ajustar_stock(request, inventario_id):
    inventario = get_object_or_404(Inventario, id=inventario_id)

    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
        tipo = request.POST['tipo']

        if tipo == 'sumar':
            inventario.stock += cantidad
        else:
            inventario.stock -= cantidad
            if inventario.stock < 0:
                inventario.stock = 0

        inventario.save()
        return redirect('inventario')

    return render(request, 'empleados/ajustar_stock.html', {
        'inventario': inventario
    })

@login_required
def pos(request):
    return render(request, 'empleados/pos.html')

@login_required
def productos(request):
    return render(request, 'empleados/productos.html')

@login_required
def pos(request):
    productos = Presentacion.objects.select_related('producto')
    ticket = request.session.get('pos', {})

    total = sum(
        item['precio'] * item['cantidad']
        for item in ticket.values()
    )

    return render(request, 'empleados/pos.html', {
        'productos': productos,
        'ticket': request.session.get('ticket', {}),
        'total': total
    })


@login_required
def pos_agregar(request, presentacion_id):
    ticket = request.session.get('pos', {})
    pres = get_object_or_404(Presentacion, id=presentacion_id)
    pid = str(pres.id)

    if pid in ticket:
        ticket[pid]['cantidad'] += 1
    else:
        ticket[pid] = {
            'nombre': f"{pres.producto.nombre} {pres.tamano}{pres.unidad_medida}",
            'precio': float(pres.precio),
            'cantidad': 1
        }

    request.session['pos'] = ticket
    return JsonResponse({'ok': True})


@login_required
def pos_quitar(request, presentacion_id):
    ticket = request.session.get('pos', {})
    pid = str(presentacion_id)

    if pid in ticket:
        ticket[pid]['cantidad'] -= 1
        if ticket[pid]['cantidad'] <= 0:
            del ticket[pid]

    request.session['pos'] = ticket
    return JsonResponse({'ok': True})


@login_required
def pos_cobrar(request):
    ticket = request.session.get('ticket', {})
    if not ticket:
        return redirect('ventas')

    bodega = bodega.objects.first()
    total = 0

    pedido = Pedido.objects.create(
        estado='pagado',
        total=0,
        bodega=bodega,
        cliente=None
    )

    for pid, item in ticket.items():
        presentacion = Presentacion.objects.get(id=pid)

        subtotal = float(item['precio']) * item['cantidad']
        total += subtotal

        descontar_stock(
            presentacion=presentacion,
            bodega=bodega,
            cantidad=item['cantidad']
        )

        DetallePedido.objects.create(
            pedido=pedido,
            presentacion=presentacion,
            cantidad=item['cantidad'],
            precio_unitario=item['precio'],
            subtotal=subtotal
        )

    pedido.total = total
    pedido.save()

    request.session['ticket'] = {}
    return redirect('ventas')

@login_required
def cobrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, estado='pendiente')
    bodega = pedido.bodega

    if request.method == 'POST':
        try:
            for d in pedido.detallepedido_set.all():
                descontar_stock(
                    presentacion=d.presentacion,
                    bodega=bodega,
                    cantidad=d.cantidad
                )

            pedido.estado = 'pagado'
            pedido.save()

        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('pedido_detalle', pedido_id)

        messages.success(request, 'Pedido cobrado correctamente')
        return redirect('pedidos_pendientes')

@login_required
def pedidos_pendientes(request):
    pedidos = Pedido.objects.filter(
        estado='pendiente'
    ).select_related('bodega')

    return render(request, 'empleados/pedidos_pendientes.html', {
        'pedidos': pedidos
    })

@login_required
def pedido_detalle(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    return render(request, 'empleados/pedido_detalle.html', {
        'pedido': pedido
    })

@login_required
def entregar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, estado='pagado')

    if request.method == 'POST':
        pedido.estado = 'entregado'
        pedido.save()
        messages.success(request, 'Pedido entregado')
        return redirect('pedidos_pendientes')
    
@login_required
def cancelar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, estado='pendiente')

    if request.method == 'POST':
        pedido.estado = 'cancelado'
        pedido.save()
        messages.warning(request, 'Pedido cancelado')
        return redirect('pedidos_pendientes')