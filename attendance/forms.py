from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = '__all__'

        widgets = {

            'date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }