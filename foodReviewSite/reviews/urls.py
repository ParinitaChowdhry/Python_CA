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
    path("<int:restaurant_id>/review", views.review, name="review")
    # path("review", views.review, name="review")
]