from django import forms
from django.forms import ModelForm
from .models import Review

# class ReviewForm(forms.Form):
#     review = forms.CharField(label='Review', max_length=2000)
#     rating = forms.FloatField(label='Rating')

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields=['description', 'rating']
    # review = forms.CharField(label='Review', max_length=2000)
    # rating = forms.FloatField(label='Rating')

    #     description= models.CharField(max_length=2000)
    # rating = models.FloatField(default=0.00)