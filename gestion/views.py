from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm

# Create your views here.
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestion/listar_categorias.html', {'categorias':categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
        
    else:
        form = CategoriaForm()
    return render(request, 'gestion/crear_categoria.html', {'form':form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestion/editar_categoria.html', {'form':form})

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect('listar_categorias')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/listar_productos.html', {'productos':productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
        
    else:
        form = ProductoForm()
    return render(request, 'gestion/crear_producto.html', {'form':form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')        
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestion/editar_producto.html', {'form':form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('listar_productos')