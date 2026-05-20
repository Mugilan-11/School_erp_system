from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = '__all__'

        widgets = {

            'student': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

        }


class AttendanceExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )

    )