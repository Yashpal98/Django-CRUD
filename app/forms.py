from django import forms
from .models import Person, gender_choice, hobby_choice


# class PersonForm(forms.Form):
#     gender = forms.ChoiceField(choices=gender_choice, widget=forms.RadioSelect, required=True)
#     # hobby = forms.ChoiceField(choices=hobby_choice, widget=forms.CheckboxSelectMultiple, required=True)
#     hobby = forms.MultipleChoiceField(choices=hobby_choice, widget=forms.CheckboxSelectMultiple, required=True)
#     # gender = forms.ChoiceField(choices=gender_choice, required=True)

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ("__all__")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.RadioSelect
           }