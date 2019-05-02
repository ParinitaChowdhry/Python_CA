from django import forms

class ReviewForm(forms.Form):
    your_review = forms.CharField(label='Your review', max_length=1000)