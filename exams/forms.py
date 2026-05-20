from django import forms
from .models import ExamResult


class ExamResultForm(forms.ModelForm):

    class Meta:

        model = ExamResult

        fields = [
            'student',
            'exam_name',
        ]