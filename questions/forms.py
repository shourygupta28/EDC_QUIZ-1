from .models import Answer
from django import forms

class AnswerForm(forms.ModelForm):
    CHOICES = [('A', 'A'),
               ('B', 'B'),
               ('C', 'C'),
               ('D', 'D')]

    answer1     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer2     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer3     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer4     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer5     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer6     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer7     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer8     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer9     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer10    = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer11    = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer12    = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)
    answer13    = forms.CharField(widget=forms.Textarea, required=False)
    answer14    = forms.CharField(widget=forms.Textarea, required=False)
    answer15    = forms.CharField(widget=forms.Textarea, required=False)

    class Meta: 
        model = Answer
        fields = ['answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'answer6', 'answer7', 'answer8', 'answer9', 'answer10', 'answer11', 'answer12', 'answer13', 'answer14', 'answer15']