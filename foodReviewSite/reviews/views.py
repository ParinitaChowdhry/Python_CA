from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Restaurant, Review, Comment
from .forms import ReviewForm, CommentForm, UserForm
from django.contrib.auth.models import User
from datetime import datetime
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# view of all categories from DB
def cat_list(request):
    if request.user.is_authenticated:
        context = {"categories": Restaurant.category_choices}
        return render(request, "cat_list.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))

# view of list of restaurant which belong to a particular category
def rest_list(request, category_id):
    if request.user.is_authenticated:
        try:
            restaurant = Restaurant.objects.filter(category=category_id)
        except Restaurant.DoesNotExist:
            raise Http404("Restuarant does not exist")
        context = {"restaurants": restaurant}
        return render(request, "rest_list.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))

# view reviews of selected restaurant
def rest_detail(request, restaurant_id):
    if request.user.is_authenticated:
        try:
            restaurant= Restaurant.objects.get(pk=restaurant_id)
            review_exist = True
        except Restaurant.DoesNotExist:
            raise Http404("Restuarant does not exist")
        review = Review.objects.filter(user=request.user, restaurant=restaurant)
        if not review:
            review_exist = False
        context = {"restaurant" : restaurant, 
        "reviews" : Review.objects.filter(restaurant=restaurant), 
        "review_exist" : review_exist,
        "review": review}
        return render(request, "rest_detail.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))

# submit review of selected restaurant
def review(request, restaurant_id):
    if request.user.is_authenticated:
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404("Restuarant does not exist")
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                desc = form.cleaned_data['description']
                rating = form.cleaned_data['rating']
                review = Review(user=request.user, restaurant=restaurant, description = desc, rating = rating)
                review.save()
                return HttpResponseRedirect(reverse('cat_list'))
            else:
                return render(request, 'review.html', {'form': form})
        if request.method == 'GET':
            form=ReviewForm()
            return render(request, 'review.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('login'))


# submit review of selected restaurant
def review_detail(request, review_id):   
    # u = User.username- add in later
    if request.user.is_authenticated:
        try:
            review= Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise Http404("Review does not exist")
        context = {
            "review": review,
            "comments" : Comment.objects.filter(review=review)
            }
        return render(request, "review_detail.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))

# submit review of selected restaurant
def comment(request, review_id):   
    # u = User.username- add in later
    if request.user.is_authenticated:
        try:
            review= Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise Http404("Review does not exist")
        if request.method == 'POST':
            form = CommentForm(request.POST)
        # check whether it's valid:
            if form.is_valid():
                desc = form.cleaned_data['content']
                comment = Comment(user=request.user, review = review, content=desc)
                comment.save()
                return HttpResponseRedirect(reverse('cat_list'))
            else:
                return render(request, 'comment.html', {'form': form})
        if request.method == 'GET':
            form=CommentForm()
            return render(request, 'comment.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('login'))        

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
            return HttpResponseRedirect(reverse('cat_list'))
        if user is None:
            return render(request, 'login.html', {'message': 'Invalid credentials'})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    else:
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


