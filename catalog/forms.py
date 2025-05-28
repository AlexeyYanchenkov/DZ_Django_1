from django import forms
from django.core.exceptions import ValidationError
from .models import Product

# Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Слово '{word}' недопустимо в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Слово '{word}' недопустимо в описании продукта.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
