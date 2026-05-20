from django import forms
from .models import Timetable


class TimetableForm(forms.ModelForm):

    class Meta:

        model = Timetable

        fields = '__all__'

        widgets = {

            'class_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'teacher': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'day': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'start_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

            'end_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

        }


class TimetableExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )

    )