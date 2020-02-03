from django.shortcuts import render

from .forms import ListingsForm, RawListingsForm

from .models import Listings
# Create your views here.

# def listings_create_view(request):

# 	my_form = RawListingsForm()
# 	if request.method == "POST":
# 		my_form = RawListingsForm(request.POST)
# 	if my_form.is_valid():
# 		# Now Data is good as validations is done
# 		print(my_form.cleaned_data)
# 		Listings.objects.create(**my_form.cleaned_data)
# 	else:
# 		print(my_form.errors)

# 	context = {
# 		"form": my_form
# }
# 	return render(request,"listings/listings_create.html", context)





# def listings_create_view(request):
# 	#print(request.GET)
# 	#print(request.POST)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 	# Listings.objects.create(title= my_new_title)
# 	context = {}
# 	return render(request,"listings/listings_create.html", context)

def listings_create_view(request):
	form = ListingsForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ListingsForm()

	context = {
		'form' : form

	}
	return render(request,"listings/listings_create.html", context)


def listings_detail_view(request):
		obj = Listings.objects.get(id=1)
	 #context = {
	#	'title': obj.title,
	#	'description': obj.description,
	#	'price': obj.price,
	#	'summary': obj.summary,
	#	'featured': obj.featured
#
#
	#}
		context = {
		'object' : obj

	}
		return render(request,"listings/listings_detail.html", context)