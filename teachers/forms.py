from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:

        model = Teacher

        fields = '__all__'

        widgets = {

            'user': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'employee_id': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

        }