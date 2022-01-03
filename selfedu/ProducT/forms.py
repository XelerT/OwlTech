from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput
# from tinymce.widgets import TinyMCE

from ProducT.models import Product

class CreationForm(ModelForm):

    # product_name = forms.CharField(max_length=100, help_text="Required. Add a valid product name.")
    # content_math    = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Product
        fields = ('product_name', 'product_descr', 'product_type', 'product_video', 'product_file', 'product_creator', 'content', )

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        try:
            product = Product.objects.get(product_name=product_name)
        except Exception as e:
            return product_name
        raise forms.ValidationError(f"Name {product_name} is already in use.")
