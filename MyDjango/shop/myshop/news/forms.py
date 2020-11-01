from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок новости', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст новости', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    is_published = forms.BooleanField(label='Опубликовать', initial=True)
    category = forms.ModelChoiceField(empty_label='Без категории', queryset=Category.objects.all(), label='Категория новости', widget=forms.Select(attrs={"class": "form-control"}))