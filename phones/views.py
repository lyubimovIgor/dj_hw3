import csv

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from phones.models import Phone

def index(request):
    # Очистка таблицы Phone перед загрузкой данных из файла
    Phone.objects.all().delete()

    # Чтение данных из файла phones.csv и создание записей Phone
    with open('phones.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            Phone.objects.create(
                id=row['id'],
                name=row['name'],
                image=row['image'],
                price=row['price'],
                release_date=row['release_date'],
                lte_exists=row['lte_exists'],
                slug=slugify(row['name'])
            )

    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        context = {'phones': Phone.objects.all().order_by('name')}
    elif sort == 'min_price':
        context = {'phones': Phone.objects.all().order_by('price')}
    elif sort == 'max_price':
        context = {'phones': Phone.objects.all().order_by('-price')}

    else:
        context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug=slug)[0]}
    print(Phone.objects.filter(slug=slug)[0].name)
    return render(request, template, context)