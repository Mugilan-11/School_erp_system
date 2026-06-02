from django import forms


class ExtractorUploadForm(forms.Form):

    excel_file = forms.FileField()


class RowSelectionForm(forms.Form):

    header_row = forms.IntegerField(
        min_value=1,
        initial=6,
        label="Header Row"
    )

    start_row = forms.IntegerField(
        min_value=1,
        initial=7,
        label="Start Data Row"
    )

    end_row = forms.IntegerField(
        min_value=1,
        initial=40,
        label="End Data Row"
    )