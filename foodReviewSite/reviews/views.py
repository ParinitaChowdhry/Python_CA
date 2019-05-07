from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Review, Comment
from .forms import ReviewForm, CommentForm
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
    restaurant= Restaurant.objects.get(pk=restaurant_id)
    context = {
        "restaurant" : restaurant,
         "reviews" : Review.objects.filter(restaurant=restaurant)
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
        # context = {
        # "restaurant" : r
        # }
        # return render(request, 'review.html', {'form': form}, context)
        return render(request, 'review.html', {'form': form})

# submit review of selected restaurant
def review_detail(request, review_id):   
    # u = User.username- add in later
    review= Review.objects.get(pk=review_id)
    context = {
        "review": review,
        "comments" : Comment.objects.filter(review=review)
    }
    return render(request, "review_detail.html", context)

# submit review of selected restaurant
def comment(request, review_id):   
    # u = User.username- add in later
    review= Review.objects.get(pk=review_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            desc = form.cleaned_data['content']
            comment = Comment(review = review, content=desc)
            comment.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'comment.html', {'form': form})
    if request.method == 'GET':
        form=CommentForm()
        # context = {
        # "review" : review
        # }
        # return render(request, 'comment.html', {'form': form}, context)
        return render(request, 'comment.html', {'form': form})
