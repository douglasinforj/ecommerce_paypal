from django.shortcuts import render
from .models import *

from django.http import JsonResponse
import json

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
        

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    #verificando se usuário esta logado
    if request.user.is_authenticated:
        #consultando os itens do carrinho
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        #criando carrinho vazio, para usuário não LOGADO, pois o nosso model vai dar um loop nos itens e precisamos passar algo []
        items = []
        #carrinho do usuário não logado, precisamos passar algo para no model consultar e esta zerado
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    #passsando itens consultado pelo contexto para o template
    context = {'items':items,'order': order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
        

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)


#view para updateItem, quando clicarmos no botão adicionar ao carrinho, enviaremos o id do produto junto com a ação de adicionar ou remover
def updateItem(request):

    data = json.loads(request.body)   #recebendo od dados de data, vindos da função (updateUserOrder) javascript
    #separando os dados:
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    #tratando order
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    #tratando a action (adicionar ou remover item)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    #deletando a quantidade com action, seguindo a condição
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse('Item Foi Adicionado', safe=False)  