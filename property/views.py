from django.views import generic
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import House, HouseAddress, HouseOwnerDetails
from .ml import estimate
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


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

#
# class DetailView(generic.DetailView):
#     model = House
#     template_name = 'property/detail.html'

def detail(request, house_id):
    house = House.objects.filter(pk__in=house_id)
    owner = HouseOwnerDetails.objects.filter(house__in=house)
    address = HouseAddress.objects.filter(house__in=house)
    return render(request, 'property/detail.html', {'detail' : zip(house, owner, address)})


def find_property(request):
    add = request.GET['address']
    area = request.GET['area']
    price1 = request.GET['price']
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
    context = { 'houses': houses, 'owners': owners,'addresses': addresses, 'filteredId': filteredId, 'mylist': zip(houses, addresses, owners)}
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
    price = estimate(mszone, mssubclass, utilities, street, salecondition, overallqual, garagecars, garagearea, bsmtarea, fstfloorarea, fullbath, yearbuilt,
                     lotarea, kitchen, lotarea)
    features = {'mszone':mszone, 'mssubclass':mssubclass, 'utilities':utilities, 'street':street, 'salecondition':salecondition, 'overallqual': overallqual, 'garagecars':garagecars, 'garagearea':garagearea,
                                                     'bsmtarea': bsmtarea, 'fstfloorarea':fstfloorarea, 'fullbath':fullbath, 'yearbuilt':yearbuilt, 'lotarea':lotarea,
                                                     'kitchen':kitchen,}
    return render(request, 'property/predict.html', {'price':round(price), 'features':features.items()})

def contactus(request):
    name = request.POST.get('name')
    subject = 'Query On Website from '
    from_email = request.POST.get('email')
    to = 'deepakcsgn@gmail.com'
    message = request.POST.get('msg')
    try:
        send_mail(subject, message, from_email, [to], fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponse("<h1>Query successfully placed with us</h1><p>We will catch you within a week</p>")


def houselist(request):
    ids = House.objects.all().values_list('id', flat=True)
    print(ids)
    address = HouseAddress.objects.all()
    house = House.objects.all()
    owner = HouseOwnerDetails.objects.all()
    context = {'ids' : ids, 'address': address, 'house': house, 'owner': owner, 'mylist' : zip(house, address, owner)}
    return render(request, 'property/propertylist.html', context)


@login_required
def home(request):
    return render(request, 'property/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'property/signup.html', {'form': form})


def add(request):
    if request.method == 'POST' and request.FILES['property_pic']:
        house_no = request.POST.get('house_no')
        registry_no = request.POST.get('registry_no')
        property_pic = request.FILES.get('property_pic')
        property_type = request.POST.get('property_type')
        property_style = request.POST.get('property_style')
        property_region = request.POST.get('property_region')
        size = request.POST.get('size')
        no_of_kitchen = request.POST.get('no_of_kitchen')
        no_of_bedroom = request.POST.get('no_of_bedroom')
        no_of_bathroom = request.POST.get('no_of_bathroom')
        year_built = request.POST.get('year_built')
        price = request.POST.get('price')

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        district = request.POST.get('district')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('gender')
        pin = request.POST.get('pin')

        block = request.POST.get('block')
        sec = request.POST.get('sec')
        area = request.POST.get('area')
        landmark = request.POST.get('landmark')
        hstate = request.POST.get('hstate')
        country = request.POST.get('country')
        hpin = request.POST.get('hpin')

        a = House(house_no=house_no, registry_no=registry_no, property_pic=property_pic, property_style=property_style, property_region=property_region,
                  property_type=property_type, size=size, no_of_bathroom=no_of_bathroom, no_of_bedroom=no_of_bedroom, no_of_kitchen=no_of_kitchen,
                  year_built=year_built, price=price)
        a.save()
        b=HouseOwnerDetails(house=a, firstname=firstname, lastname=lastname, contact_no=contact_no, email=email, city=city, state=state, district=district,
                            address=address, gender=gender, age=age, pin=pin)
        b.save()
        c=HouseAddress(house=a, block=block, sec=sec, area=area, landmark=landmark, state=hstate, country=country, pin=hpin)
        c.save()
        return render(request, 'succeesful')
    else:
        return render(request, 'property/addhouse.html')

def adddetail(request):
    return render(request, 'property/signup.html')
