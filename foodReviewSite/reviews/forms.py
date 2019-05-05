from django import forms
from django.forms import ModelForm, DecimalField
from .models import Review
from django.core.validators import MaxValueValidator, MinValueValidator

class ReviewForm(ModelForm):
    rating = DecimalField(validators=[ MaxValueValidator(5.0),MinValueValidator(0.1)])

    class Meta:
        model = Review
        fields=['description', 'rating']