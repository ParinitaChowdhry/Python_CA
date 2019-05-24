from django.test import TestCase, Client
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Restaurant, Review, Comment

# dont how to test login, logout n register
# not tested yet

# Create your tests here.
class FlightsTestCase(TestCase):

    def setUp(self):

        # Create restuarant: category 1, 2 and 3
        test_restaurant_1 = Restaurant.objects.create(id=1, name="restaurant_1", address="location_1", category=1)
        test_restaurant_2 = Restaurant.objects.create(id=2, name="restaurant_2", address="location_2", category=1)
        test_restaurant_2 = Restaurant.objects.create(id=3, name="restaurant_3", address="location_3", category=2)

        # Create User
        test_user_1 = User.objects.create(username="user_1", password="password")
        test_user_2 = User.objects.create(username="user_2", password="password")

        # Create reviews
        Review.objects.create(user=test_user_1, restaurant=test_restaurant_1, description = "very good", rating = 1)

        # Count of Reviews for restaurant restaurant_1 should be 1 
    def test_reviews_count(self):
        rest = Restaurant.objects.get(name="restaurant_1")
        get_review = rest.review_set.all()
        self.assertEqual(get_review.count(), 1)    

        # error
        # No restaurant with category 6 : does not exist
    # def test_restaurant(self):
    #     rest = Restaurant.objects.get(category=6)
    #     self.assertEqual(rest.count(), 0)

    #     # error
    #     # count of users with username user_1
    # def test_user(self):
    #     user = User.objects.get(username="user_1")
    #     self.assertEqual(user.count(), 1)
    #     # no attribute count

        # failed
        # count of no of categories
    def test_valid_cat_list_page(self):
        c = Client()
        response = c.get(f"category")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["categories"].count(), 6)

        # no restaurant with maximum category outside Restaurant.category_choices
    def test_invalid_rest_list_page(self):
        cat_list = Restaurant.category_choices
        max_cat = sum(1 for e in cat_list)
        c = Client()
        response = c.get(f"category/{max_cat + 1}")
        self.assertEqual(response.status_code, 404)

        # category 1 has two restaurant
    def test_valid_rest_list_page(self):
        # cat = 1
        c = Client()
        response = c.get(f"category/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["restaurants"].count(), 2)

        # no restaurant with maximum id more than DB
    def test_invalid_rest_detail(self):
        max_rest_id = Restaurant.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"category/{max_rest_id + 1}/detail")
        self.assertEqual(response.status_code, 404)

        # failed
        # details for restaurant 1
    def test_valid_rest_detail(self):
        # rest_id = 1
        c = Client()
        response = c.get(f"category/1/detail")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["restaurant"].count(), 1)
        self.assertEqual(response.context["restaurant"]["name"], "restaurant_1")
        self.assertEqual(response.context["restaurant"]["address"], "location_1")
        self.assertEqual(response.context["restaurant"]["category"], 1)
        self.assertEqual(response.context["reviews"].count(), 1)
        for e in response.context["reviews"]:
            self.assertEqual(e["description"], "very good")
            self.assertEqual(e["rating"], 1)
            self.assertEqual(e["user"]["username"], "user_1")

    # def test_flight_page_non_passengers(self):
    #     f = Flight.objects.get(pk=1)
    #     p = Passenger.objects.create(first="Alice", last="Adams")

    #     c = Client()
    #     response = c.get(f"/{f.id}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["non_passengers"].count(), 1)
            
    # def test_valid_flight(self):
    #     rest = Restaurant.objects.get(name="AAA")
    #     review = Review.objects.get(restaurant=rest)
    #     self.assertTrue(f.is_valid_flight())

    # def test_invalid_flight_destination(self):
    #     a1 = Airport.objects.get(code="AAA")
    #     f = Flight.objects.get(origin=a1, destination=a1)
    #     self.assertFalse(f.is_valid_flight())

    # def test_invalid_flight_duration(self):
    #     a1 = Airport.objects.get(code="AAA")
    #     a2 = Airport.objects.get(code="BBB")
    #     f = Flight.objects.get(origin=a1, destination=a2)
    #     f.duration = -100
    #     self.assertFalse(f.is_valid_flight())

    # def test_login(self):
    #     c = Client()
    #     response = c.get("/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.context["flights"].count(), 2)

