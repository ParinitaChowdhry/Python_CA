from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Review, Comment
from .forms import ReviewForm, CommentForm, UserForm
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout

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

def login_user(request):
    if request.method =='GET':
        form=UserForm()
        return render(request, 'login.html', {'form': form})
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.filter(username=username, password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        if user is None:
            return render(request, 'login.html', {'message': 'Invalid credentials'})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method =='GET':
        form=UserForm()
        return render(request, 'register.html', {'form': form})
    if request.method =='POST':
         form = UserForm(request.POST)
         # check whether it's valid:
         if form.is_valid():
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user = User.objects.create_user(username)
             user.set_password(form.cleaned_data['password'])
             user.save()
             return HttpResponseRedirect(reverse('login'))
         else:
             return render(request, 'register.html', {'form': form})

def user(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "user.html", context)
    

    # path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),
    # path("register", views.register, name="register")
