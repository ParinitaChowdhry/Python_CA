from django.urls import path

from . import views

urlpatterns = [
    # index view
    path("", views.index, name="index"),
    # list of restaurant of a category
    path("category/<int:category_id>", views.rest_list, name="rest_list"),
    # reviews of restaurant selected
    path("category/<int:restaurant_id>/detail", views.rest_detail, name="rest_detail"),
    # submit review
    path("category/<int:restaurant_id>/review", views.review, name="review"),
    # comments of review selected
    path("category/review/<int:review_id>/detail", views.review_detail, name="review_detail"),
    # add comment
    path("category/review/<int:review_id>/comment", views.comment, name="comment"),
    # login
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path("user", views.user, name="user")
]


