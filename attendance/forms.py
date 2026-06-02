from django import forms
from django.core.exceptions import ValidationError

from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = "__all__"

        widgets = {

            "student": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Optional remarks",
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        student = cleaned_data.get(
            "student"
        )

        date = cleaned_data.get(
            "date"
        )

        if student and date:

            exists = (
                Attendance.objects.filter(
                    student=student,
                    date=date,
                )
                .exclude(
                    pk=self.instance.pk
                )
                .exists()
            )

            if exists:

                raise ValidationError(
                    "Attendance has already been marked for this student on this date."
                )

        return cleaned_data


class AttendanceExcelUploadForm(forms.Form):

    excel_file = forms.FileField(

        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".xlsx,.xls",
            }
        )

    )

    def clean_excel_file(self):

        excel_file = self.cleaned_data[
            "excel_file"
        ]

        allowed_extensions = (
            ".xlsx",
            ".xls",
        )

        if not excel_file.name.endswith(
            allowed_extensions
        ):

            raise ValidationError(
                "Please upload a valid Excel file."
            )

        return excel_file