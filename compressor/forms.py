from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')
    compression_level = forms.IntegerField(
        label='Compression Level',
        min_value=1,
        max_value=100,
        initial= 95,
        widget=forms.NumberInput(attrs={'type': 'range'})
    )
    

class ImageCompressForm(forms.Form):    
    compression_level = forms.IntegerField(
        label='Compression Level',
        min_value=1,
        max_value=100,
        initial= 95,
        widget=forms.NumberInput(attrs={'type': 'range'})
    )

    
class ImageDownloadForm(forms.Form):
    DOWNLOAD_CHOICES = [
        ('JPG', 'JPG'),
        ('PNG', 'PNG'),
        ('BMP', 'BMP'),
        ('TIFF', 'TIFF'),        
    ]

    download_type = forms.ChoiceField(
        label='Choose The Image Type',
        choices=DOWNLOAD_CHOICES,
        initial= 'JPG',
        widget=forms.RadioSelect(attrs={'type': 'radio'})
    )
