# blog/forms.py

from django import forms
from .models import Comment, Post, Category

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}), label='')

    class Meta:
        model = Comment
        fields = ['text']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = fields = ["title", "short_description", "cover_image", "category", "content"]

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))  # Add Bootstrap classes to title field
    short_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))  # Add Bootstrap classes to short_description field
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}))  # Add Bootstrap classes to cover_image field
    
    # Add Bootstrap classes to the category field
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select mb-2'})
    )