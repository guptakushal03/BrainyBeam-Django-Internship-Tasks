from django import forms
from .models import Question, Option

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            choices = [(option.id, option.text) for option in question.options.all()]
            correct_count = question.options.filter(is_correct=True).count()
            total_count = question.options.count()
            self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(
                choices=choices,
                widget=forms.CheckboxSelectMultiple,
                label=f"{question.text} ({correct_count} of {total_count} options correct)",
                required=True
            )
