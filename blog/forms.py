from .models import Post, Answer
from django import forms
class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)
