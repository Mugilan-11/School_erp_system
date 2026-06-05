from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
    "name",
    "student_id",
    "student_class",
    "gender",
    "date_of_birth",
    "address",
    "profile_picture",
]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter last name",
                }
            ),
            "student_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter student ID",
                }
            ),
            "student_class": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter address",
                }
            ),
            "profile_picture": forms.FileInput(
                    attrs={
                    "class": "form-control",
                }
            ),
            "name": forms.TextInput(
                attrs={
                "class": "form-control",
                "placeholder": "Enter Student Name",
                }   
            ),

            "student_id": forms.TextInput(
                attrs={
                "class": "form-control",
                "placeholder": "Enter Student ID",
                }
            ),
        }
        def save(self, commit=True):

            student = super().save(commit=False)

            student.admission_no = (
            student.student_id
            )

            if student.name:
                student.first_name = (
                student.name
            )

            if not student.last_name:
                student.last_name = ""

            if commit:
                student.save()

            return student


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".xlsx,.xls",
            }
        )
    )