from .models import Comment
from django.forms import ModelForm, TextInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "comment_text"]
        widgets = {
            "author_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "comment_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария'
            })
        }
