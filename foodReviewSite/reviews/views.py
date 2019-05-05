from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Review
from .forms import ReviewForm
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ValidationError

# Create your views here.
# view of all categories from DB
def index(request):
    context = {
        "categories": Restaurant.category_choices
    }
    return render(request, "index.html", context)

# view of list of restaurant which belong to a particular category
def rest_list(request, category_id):
    context = {
        "restaurants": Restaurant.objects.filter(category=category_id),
    }
    return render(request, "rest_list.html", context)

# view reviews of selected restaurant
def rest_detail(request, restaurant_id):
    r= Restaurant.objects.get(pk=restaurant_id)
    context = {
        "reviews" : Review.objects.filter(restaurant=r),
        "restaurant" : r
    }
    return render(request, "rest_detail.html", context)

# submit review of selected restaurant
def review(request, restaurant_id):   
    # u = User.username- add in later
    r = Restaurant.objects.get(pk=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            desc = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            review = Review(restaurant=r, description = desc, rating = rating)
            review.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'review.html', {'form': form})
    if request.method == 'GET':
        form=ReviewForm()
        context = {
        "restaurant" : r
        }
        return render(request, 'review.html', {'form': form}, context)
