from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):

    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones_objects = Phone.objects.order_by('name')
    elif sort_by == 'min_price':
        phones_objects = Phone.objects.order_by('price')
    elif sort_by == 'max_price':
        phones_objects = Phone.objects.order_by('-price')
    else:
        phones_objects = Phone.objects.all()

    phones = []
    for phone in phones_objects:
        phones.append({'id': phone.id, 'name': phone.name, 'price': phone.price, 'image': phone.image,
                       'release_date': phone.release_date, 'lte_exists': phone.lte_exists, 'slug': phone.slug})
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phones_objects = Phone.objects.filter(slug=slug)

    for phone in phones_objects:
        phones = {'name': phone.name, 'price': phone.price, 'image': phone.image,
                  'release_date': phone.release_date, 'lte_exists': phone.lte_exists}
    template = 'product.html'
    context = {'phone': phones}
    return render(request, template, context)
