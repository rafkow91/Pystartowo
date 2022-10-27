from django import forms

from dal import autocomplete

from .models import Post, ToAdd
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete'),
        label='Moduły, którego dotyczy zagadnienie'
    )

    class Meta:
        model = Post
        exclude = ['author']
        fields = [
            'title',
            'content',
            'tags',
            'image_file',
            'author',
        ]
        labels = {
            'title': 'Tytuł',
            'content': 'Wyjaśnienie zagadnienia',
            'image_file': 'Przykładowy kod',
        }


class ToAddForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete-to-add'),
        label='W którym module natrafiłeś na ten problem?'
    )

    class Meta:
        model = ToAdd
        fields = [
            'title',
            'content',
            'tags',
            'email',
        ]
        labels = {
            'title': 'Tytuł',
            'content': 'Co możemy spróbować Ci wyjaśnić?',
            'email': 'Adres email',
        }
