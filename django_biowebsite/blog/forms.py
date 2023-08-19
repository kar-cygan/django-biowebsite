from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']  # fields = '__all__'
        labels = {
            'name': 'Category name',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Category name',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Short category description',
                    'class': 'form-control'
                }
            ),          
        }
