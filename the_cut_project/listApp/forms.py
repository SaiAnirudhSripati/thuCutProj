from django import forms
from .models import List

class NewListItemForm(forms.ModelForm):
    list_desc=forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model=List
        fields=['list_name','list_desc']

    def clean(self):


        super(NewListItemForm, self).clean()


        list_name = self.cleaned_data.get('list_name')
        list_desc = self.cleaned_data.get('list_desc')


        if len(list_name) < 3:
            self._errors['list_name'] = self.error_class([
                'Minimum 3 characters required'])
        if len(list_desc) <10:
            self._errors['list_desc'] = self.error_class([
                'Minimum 3 characters required'])

        return self.cleaned_data
