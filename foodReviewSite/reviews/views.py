from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Category, Review
from .forms import ReviewForm

# Create your views here.
# view of all categories from DB
def index(request):
    context = {
        "categories": Category.objects.all()
    }
    return render(request, "index.html", context)

# view of list of restaurant which belong to a particular category
def rest_list(request, category_id):
    c = Category.objects.get(pk=category_id)
    r = Restaurant.objects.filter(category=c)
    context = {
        "restaurants": r,
        "reviews": Review.objects.filter(restaurant=r)
    }
    return render(request, "rest_list.html", context)

# view of review of restaurant which has been selected
def rest_detail(request, restaurant_id):
    r= Restaurant.objects.get(pk=restaurant_id)
    context = {
        "reviews" : Review.objects.filter(restaurant=r)
    }
    return render(request, "rest_detail.html", context)

# view of review of restaurant which has been selected
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else :
        form=ReviewForm()
        return render(request, 'review.html', {'form': form})
