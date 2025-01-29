from django import forms
from . import models

class CreateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']