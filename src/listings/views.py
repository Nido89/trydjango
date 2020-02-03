from django.shortcuts import render

from .models import Listings
# Create your views here.
def listings_detail_view(request):
	obj = Listings.objects.get(id=1)
	context = {
		'title': obj.title,
		'description': obj.description,
		'price': obj.price,
		'summary': obj.summary,
		'featured': obj.featured


	}
	return render(request,"Listing/detail.html", context)