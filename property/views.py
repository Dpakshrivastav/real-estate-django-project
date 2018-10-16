from django.views import generic
from .models import  House, HouseAddress, HouseOwnerDetails


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


# def find_property(request):
#     city = request.POST['']

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