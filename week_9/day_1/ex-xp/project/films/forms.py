from django import forms
from .models import Director,Category,Country,Film

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
