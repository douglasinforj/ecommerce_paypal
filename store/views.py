from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html',context)

def cart(request):

    #verificando se usuário esta logado
    if request.user.is_authenticated:
        #consultando os itens do carrinho
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #criando carrinho vazio, para usuário não LOGADO, pois o nosso model vai dar um loop nos itens e precisamos passar algo []
        item = []
        
    #passsando itens consultado pelo contexto para o template
    context = {'items':items}   
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)