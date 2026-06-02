from django import forms
from django.core.exceptions import ValidationError

from .models import Fee


class FeeForm(forms.ModelForm):

    class Meta:

        model = Fee

        exclude = (
            "created_at",
            "updated_at",
        )

        widgets = {

            "student": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter amount",
                    "step": "0.01",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "payment_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
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

    def clean_amount(self):

        amount = self.cleaned_data.get(
            "amount"
        )

        if amount is not None and amount <= 0:

            raise ValidationError(
                "Amount must be greater than zero."
            )

        return amount


class FeeExcelUploadForm(forms.Form):

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
