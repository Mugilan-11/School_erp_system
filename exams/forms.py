from django import forms
from django.core.exceptions import ValidationError

from .models import ExamResult


class ResultForm(forms.ModelForm):

    class Meta:

        model = ExamResult

        exclude = (
            "created_at",
            "updated_at",
            "total_marks",
            "percentage",
            "grade",
        )

        widgets = {

            "student": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "exam_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter exam name",
                }
            ),
        }

    def clean_exam_name(self):

        exam_name = self.cleaned_data.get(
            "exam_name"
        )

        if not exam_name:

            raise ValidationError(
                "Exam name is required."
            )

        return exam_name.strip()


class ResultExcelUploadForm(forms.Form):

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

        if not excel_file.name.endswith(
            (
                ".xlsx",
                ".xls",
            )
        ):

            raise ValidationError(
                "Please upload a valid Excel file."
            )

        return excel_file
