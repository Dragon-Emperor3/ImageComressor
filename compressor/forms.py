from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    compression_level = forms.IntegerField(
        label='Compression Level',
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={'type': 'range'})
    )