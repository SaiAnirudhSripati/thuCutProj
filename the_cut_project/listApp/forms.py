from django import forms
from .models import List

class NewListItemForm(forms.ModelForm):
    list_desc=forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model=List
        fields=['list_name','list_desc']
