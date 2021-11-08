from django.shortcuts import render,redirect
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    # search code
    item_name = request.GET.get('book_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(name__icontains=item_name)

    # pagination
    paginator = Paginator(product_objects, 9)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request, 'books/index.html', {'product_objects': product_objects})


def mybooks(request):
    product_objects = Products.objects.filter(user=request.user)    
    return render(request, 'books/rentedbooks.html', {'product_objects': product_objects})


def detail(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product = Products.objects.get(id=id)
            product.count = product.count - 1
            product.user.add(request.user)
            product.save()
            return redirect('index')
        else:
            return redirect('login')
    else:
        product_object = Products.objects.get(pk=id)
        return render(request, 'books/detail.html', {'product_object': product_object})


def back(request, id):
    if request.method == 'POST':
        product = Products.objects.get(id=id)
        product.count = product.count + 1
        product.user.remove(request.user)
        product.save()
        return redirect('mybooks')