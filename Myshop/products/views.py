from django.shortcuts import render
from .models import Product, ProductCategory


def build_template(lst: list, cols: int) -> list[list]:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]


def katalog(request, pk):
    categories = ProductCategory.objects.all()
    return render(request, 'products/katalog.html', context={
        'categories': categories,
        }
                )
def products(request, **kwargs):
    pk = kwargs.get('pk')
    categories = ProductCategory.objects.all()
    category = ProductCategory.objects.get(pk=pk)
    products = category.products.all()
    return render(request, 'products/tovars.html', context={
        'products': build_template(products, 3),
        'categories': categories,
        'category': category
        }
    )
