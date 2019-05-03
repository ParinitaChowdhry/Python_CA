from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

# Create your models here.
# class Category (models.Model):
#     name= models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.name}"

class Restaurant (models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # category= models.ForeignKey(Category, on_delete=models.CASCADE)
    category_choices = (
    (1,'Western'),
    (2,'Japanese'),
    (3,'Chinese'),
    (4,'Korean'),
    (5,'Indian'),
    (6, 'Thai'),
    )
    category = models.IntegerField(choices=category_choices, default=1,)

    def __str__(self):
        return f"{self.name} - {self.address}"

class Review (models.Model):
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description= models.CharField(max_length=2000)
    rating = models.FloatField(default=0.00)
    reviewInputDateTime= models.DateTimeField('date published')

    def __str__(self):
        return f"{self.description} - {self.rating} - {self.reviewInputDateTime}"

class Comment (models.Model):
    review= models.ForeignKey(Review, on_delete=models.CASCADE)
    content= models.CharField(max_length=1000)
    commentInputDateTime= models.DateTimeField('date published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Like (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review= models.ForeignKey(Review, on_delete=models.CASCADE)