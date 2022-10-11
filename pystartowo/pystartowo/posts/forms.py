from django import forms

from dal import autocomplete

from .models import Post, ToAdd
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
        )

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
            'image_file',
        ]


class ToAddForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = ToAdd
    #     fields = "__all__"
