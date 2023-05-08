from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from account.models import User
from comparison.models import Order, ProductsInOrder
from catalog.models import Product

def add_to_comparison(request):
    path = request.GET.get('next')

    if request.method == 'POST':
        product_id = request.GET.get('product_id')

        if 'comparison' not in request.session:
            request.session['comparison'] = {}

        cart = request.session.get('comparison')

        if product_id in cart:
            cart[product_id]['quantity'] += 1

        else:
            cart[product_id] = {
                'quantity': 1
            }

    request.session.modified = True
    return redirect(path)


def view_comparison(request):
    path = request.GET.get('next')

    context = {
        'next': path,
    }

    comparison = request.session.get('comparison', None)

    if comparison:
        products = {}
        product_list = Product.objects.filter(pk__in=comparison.keys()).values('id', 'title', 'description_little', 'image')

        for product in product_list:
            products[str(product['id'])] = product

        for key in comparison.keys():
            comparison[key]['product'] = products[key]

        context['comparison'] = comparison

    return render(request, 'comparison.html', context)


@login_required(login_url='login')
def view_order(request):
    if request.method == 'POST':
        user_id = request.user.pk
        customer = User.objects.get(pk=user_id)

        comparison = request.session['cart']

        if len(comparison) > 0:
            order = Order.objects.create(customer=customer)

            for key, value in comparison.items():
                product = Product.objects.get(pk=key)
                quantity = value['quantity']
                ProductsInOrder.objects.create(order=order, product=product, quantity=quantity)

            request.session['comparison'] = {}
            request.session.modified = True

            messages.success(request, 'Заказ принят')

    return redirect('comparison:comparison')
