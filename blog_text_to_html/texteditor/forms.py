from dataclasses import field
from pyexpat import model
from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget


class Editorform(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget, label='Text Editor')

    class Meta:
        model = Editor
        fields = "__all__"
