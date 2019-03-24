from django import forms
from django.forms.models import inlineformset_factory

from .models import Choice, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )


ChoiceFormSet = inlineformset_factory(
    parent_model=Question, model=Choice, form=QuestionForm,
    extra=2, max_num=10, can_delete=False
)
