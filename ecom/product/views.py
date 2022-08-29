from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Cart
from .models import Product, Category
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def get_products(request, slug):
    try: 
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        if request.GET.get('size'):
            size =request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price)
        return render(request, 'product/product.html', context = context)
    except Exception as e:
        print(e)
        
        
def add_to_cart(request, slug):
    variant = request.GET.get('variant')
    product = Product.objects.get(slug=slug)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    
    
    return HttpResponseRedirect(request.path_info)