from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:

        model = Teacher

        exclude = (
            "created_at",
            "updated_at",
        )

        widgets = {

            "user": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                }
            ),

            "employee_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Employee ID",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Subject",
                }
            ),

            "qualification": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Qualification",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),

            "joining_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Address",
                }
            ),

            "profile_picture": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
