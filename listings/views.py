from django.shortcuts import get_object_or_404,render
from .models import Listing
from listings.choices import price_choices,bedroom_choices,state_choices
def index(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings,
        }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    # listing = Listing.objects.first()
    print(listing.id)

    context = {'listing' : listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    context ={
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request, 'listings/search.html')

