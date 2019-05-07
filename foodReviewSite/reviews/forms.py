from django import forms
from django.forms import ModelForm
from .models import Review, Comment

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields=['description', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=['content']