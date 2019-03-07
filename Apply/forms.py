from django import forms
from .models import Apply, Evaluation

class ApplyForm(forms.Form):
    apply_name = forms.CharField(max_length=45)
    apply_schoolNum = forms.CharField(max_length=45)
    apply_phone = forms.CharField(max_length=45)
    apply_department = forms.CharField(max_length=45)
    apply_location = forms.CharField(max_length=45)
    apply_email = forms.CharField(max_length=45)
    apply_question1 = forms.CharField(widget=forms.Textarea)
    apply_question2 = forms.CharField(widget=forms.Textarea)
    apply_question3 = forms.CharField(widget=forms.Textarea)

class EvaluationForm(forms.Form):
    CHOICES=[
        ('1', 'point1'),
        ('2', 'point2'),
        ('3', 'point3'),
        ('4', 'point4'),
        ('5', 'point5'),
    ]
    
    apply_point1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='답변 1')
    apply_point2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='답변 2')
    apply_point3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='답변 3')
    apply_point_comment = forms.CharField(widget=forms.Textarea, label='총 평')