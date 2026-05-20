from django import forms
from .models import Fee


class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        fields = '__all__'

        widgets = {

            'student': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'amount': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
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

        }


class FeeExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )

    )