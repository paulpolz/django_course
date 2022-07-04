from django import forms
from app_storage.models import Article


class CartAddStockForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['stock']
        widgets = {
            'stock': forms.NumberInput(),
        }

class CreateOrderButtonForm(forms.Form):
    pass