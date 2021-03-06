from django.shortcuts import render
from django.http import HttpResponse
from BeersApp.models import Places, Beer  #check if syntacs is correct here

def search_brand(request):
    return render(request, 'search_brand_in_db.html')

# this view's aim is to show the search_place_form.html template via which the search for places is performed

#def search(request):
 #   if 'q' in request.GET:
  #      message = 'You searched for: %r' % request.GET['q']
   # else:
    #    message = 'You submitted an empty form.'
    #return HttpResponse(message)

# this view handels the url to which the submitted form is passed. if a user submitted an empty string -'q', it won't exist in request.GET

def search_brand_results(request):
    if 'q' in request.GET and request.GET['q']: # q is not an empty value
        q = request.GET['q']
        brands = Beer.objects.filter(brand__icontains=q)
        return render(request, 'search_brand_results.html',
            {'brands': brands, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def index (request):
    brands_lst=list(Beer.objects.all())
    desired_column_length = 2
    brands = [[]]
    col = brands[0]
    while len(brands_lst):
        col.append(brands_lst.pop())
        if len(col)>=desired_column_length:
                newcol = []
                brands.append(newcol)
                col = newcol

    return render(request, 'home.html', {'brands': brands})

def product(request,product_id):
    brand  = Beer.objects.get(pk=product_id)
    return render(request,'product.html',{'brand':brand})