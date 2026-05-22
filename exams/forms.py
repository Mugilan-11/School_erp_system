from django import forms

from .models import ExamResult


# =====================================
# RESULT FORM
# =====================================

class ResultForm(forms.ModelForm):

    class Meta:

        model = ExamResult

        fields = '__all__'

        widgets = {

            'student': forms.Select(

                attrs={

                    'class': 'form-control'

                }

            ),

            'subject': forms.TextInput(

                attrs={

                    'class': 'form-control'

                }

            ),

            'marks': forms.NumberInput(

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


# =====================================
# EXCEL IMPORT FORM
# =====================================

class ResultExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(

            attrs={

                'class': 'form-control'

            }

        )

    )