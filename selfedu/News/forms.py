from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput
from PIL import Image

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'text', 'date']
        widgets = {
            # 'Img': Image.open('webCoding/media_cdn/image_2021-09-16_20-50-04.png', "rb"),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'subtitle': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtitle'
            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Y-M-D XX:XX:XX'
            })
        }
