from django import forms
from django.forms import ModelForm, DecimalField
from .models import Review
from django.core.validators import MaxValueValidator, MinValueValidator

class ReviewForm(ModelForm):

    class Meta:
        model = Review
        fields=['description', 'rating']