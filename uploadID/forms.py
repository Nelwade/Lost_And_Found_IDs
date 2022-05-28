from django import forms

class UploadForm(forms.Form):
    ID_num = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter ID number'})
        )
    Location_found = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Location Found'})
    )
    Image = forms.ImageField()
    Pick_up_location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Pick Up Location'})
    )
    contact = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Contact Information'})
    )