from django import forms
from .models import Category


class GifForm(forms.Form):
    title = forms.CharField(max_length=100)
    uploader_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Uploader name',
            }
        )
    )
    url = forms.URLField()
    field_order = ['title', 'uploader_name', 'url']
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all()
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','gifs']