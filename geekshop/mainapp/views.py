from django.shortcuts import render
from datetime import datetime

# Create your views here.
mainapp_list = [{'view_name': 'index', 'link_name': 'домой'}, {'view_name': 'products', 'link_name': 'Продукты'},
                {'view_name': 'contact', 'link_name': 'Контакты'},
                ]


def index(request):
    return render(request, 'mainapp/index.html', context={
        'now_date': datetime.now(),
        'name': 'jarno',
        'mainapp_list': mainapp_list,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'now_date': datetime.now(),
        'name': 'jarno',
        'mainapp_list': mainapp_list,
    })


def products(request):
    return render(request, 'mainapp/products.html', context={
        'now_date': datetime.now(),
        'name': 'jarno',
        'mainapp_list': mainapp_list,
        'product_types': ['все', 'дом', 'офис', 'модерн', 'классика'],
    })
