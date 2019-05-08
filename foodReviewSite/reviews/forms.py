from django import forms
from django.forms import ModelForm
from .models import Review, Comment
from django.contrib.auth.models import User

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields=['description', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=['content']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields=['username', 'password']
        