from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = '__all__'

        widgets = {

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name'
                }
            ),

            'admission_no': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter admission number'
                }
            ),

            'student_class': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Enter address'
                }
            ),

            'profile_picture': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class ExcelUploadForm(forms.Form):

    excel_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )