from django.shortcuts import render
from .models import Destination
from .forms import DestinationForm, RawDestinationForm

# Create your views here.

def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})

def destinationCreateView(request):
    if request.method == 'POST':
        name=request.POST['name']
        img = request.FILES['img']
        desc = request.POST['desc']
        price = request.POST['price']
        offer = request.POST.get('offer', False)
        if offer=='on':
            offer=True
        else:
            offer=False
        my_form=Destination.objects.create(name=name, img=img, desc=desc, price=price, offer = offer)
        my_form.save()
        dests=Destination.objects.all()

    return render(request, 'destinationsCreate.html')