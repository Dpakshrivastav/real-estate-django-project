from django.views import generic
from django.db.models import Q
from django.shortcuts import render
from .models import House, HouseAddress, HouseOwnerDetails
from .ml import estimate

class IndexView(generic.ListView):
    template_name = 'property/index.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class BuyingView(generic.ListView):
    template_name = 'property/buying.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class SellingView(generic.ListView):
    template_name = 'property/selling.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class FinanceView(generic.ListView):
    template_name = 'property/finance.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class ContactView(generic.ListView):
    template_name = 'property/contacts.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class RentingView(generic.ListView):
    template_name = 'property/renting.html'
    context_object_name = 'all_houses'

    def get_queryset(self):
        return House.objects.all()


class DetailView(generic.DetailView):
    model = House
    template_name = 'property/detail.html'


def find_property(request):
    add = request.GET['address']
    area = request.GET['area']
    price1 = request.GET['price']
    price1 = int(price1)
    price2 = request.GET['price2']
    bedroom = request.GET['bedroom']
    bathroom = request.GET['bathroom']
    size = request.GET['size']
    pin = 0
    if(add.isnumeric()):
        pin = add
    # select * from house where id=(select id from house where city = add or zip = add or state = add or area = area)  AND
    houseId = HouseAddress.objects.filter(Q(state = add)|Q(area = area)).values_list('id', flat=True)
    filteredId = House.objects.filter(Q(id__in=houseId)|Q(price__range=(price1, price2))|Q(no_of_bedroom=bedroom)|Q(no_of_kitchen__lte=bathroom)|Q(size__lte=size)).values_list('id', flat=True)
    houses = House.objects.filter(id__in=filteredId)
    owners = HouseOwnerDetails.objects.filter(id__in=filteredId)
    addresses = HouseAddress.objects.filter(id__in=filteredId)
    # context = { 'address' : address, }
    context = { 'houses': houses, 'owners': owners,'addresses': addresses, 'filteredId': filteredId, }
    return render(request, 'property/search.html', context)


def mortagage(request):
    return render(request, 'property/mortagage.html')


def homevalue(request):
    return render(request, 'property/homevalue.html')


def predict(request):
    mszone = request.GET['mszone']
    mssubclass = request.GET['mszone']
    utilities = request.GET['mszone']
    street = request.GET['mszone']
    salecondition = request.GET['mszone']
    overallqual = request.GET['mszone']
    garagecars = request.GET['mszone']
    garagearea = request.GET['mszone']
    bsmtarea = request.GET['mszone']
    fstfloorarea = request.GET['mszone']
    fullbath = request.GET['mszone']
    yearbuilt = request.GET['mszone']
    lotarea = request.GET['mszone']
    kitchen= request.GET['mszone']
    price = estimate(mszone, mssubclass, utilities, street, salecondition, overallqual, garagecars, garagearea, bsmtarea, fstfloorarea, fullbath, yearbuilt, lotarea, kitchen, lotarea)
    return render(request, 'property/predict.html', {'price':price})

"""
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import House, HouseAddress, HouseOwnerDetails


app_name = 'property'


def index(request):
    all_houses = House.objects.all()
    all_address = HouseAddress.objects.all()
    all_owner = HouseOwnerDetails.objects.all()
    context = { 'all_houses': all_houses, 'all_address': all_address, 'all_owner': all_owner, }
    return render(request, 'property/index.html', context)


def detail(request, house_id):
    try:
        house = House.objects.get(pk=house_id)
        address = HouseAddress.objects.get(pk=house_id)
        owner = HouseOwnerDetails.objects.get(pk=house_id)
    except:
        raise Http404("there is an error")
    return render(request, 'property/detail.html', {'house': house, 'address': address, 'owner': owner,})
"""