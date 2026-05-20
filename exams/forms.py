from django import forms
from .models import ExamResult


class ExamResultForm(forms.ModelForm):

    class Meta:

        model = ExamResult

        fields = '__all__'

        widgets = {

            'student': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'exam_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'total_marks': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'percentage': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'grade': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }


class ResultExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )

    )