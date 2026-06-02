import io
import pandas as pd

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .forms import (
    ExtractorUploadForm,
    RowSelectionForm,
)


def extractor_upload(request):

    if request.method == "POST":

        form = ExtractorUploadForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            excel_file = request.FILES[
                "excel_file"
            ]

            df = pd.read_excel(
                excel_file,
                header=None
            )

            request.session[
                "extractor_data"
            ] = df.to_json()

            return redirect(
                "row_selection"
            )

    else:

        form = ExtractorUploadForm()

    return render(
        request,
        "extractor/upload_file.html",
        {
            "form": form,
        },
    )


def row_selection(request):

    json_data = request.session.get(
        "extractor_data"
    )

    if not json_data:

        return redirect(
            "extractor_upload"
        )

    raw_df = pd.read_json(
        io.StringIO(json_data)
    )

    preview_table = raw_df.head(
        100
    ).to_html(
        classes="table table-bordered table-striped"
    )

    if request.method == "POST":

        form = RowSelectionForm(
            request.POST
        )

        if form.is_valid():

            request.session[
                "header_row"
            ] = form.cleaned_data[
                "header_row"
            ]

            request.session[
                "start_row"
            ] = form.cleaned_data[
                "start_row"
            ]

            request.session[
                "end_row"
            ] = form.cleaned_data[
                "end_row"
            ]

            return redirect(
                "extractor_columns"
            )

    else:

        form = RowSelectionForm()

    return render(
        request,
        "extractor/row_selection.html",
        {
            "form": form,
            "preview": preview_table,
        },
    )


def extractor_columns(request):

    json_data = request.session.get(
        "extractor_data"
    )

    if not json_data:

        return redirect(
            "extractor_upload"
        )

    raw_df = pd.read_json(
        io.StringIO(json_data)
    )

    header_row = int(
        request.session.get(
            "header_row",
            1
        )
    )

    headers = raw_df.iloc[
        header_row - 1
    ]

    columns = []

    for index, value in enumerate(headers):

        if pd.isna(value):

            columns.append(
                f"Column_{index + 1}"
            )

        else:

            columns.append(
                str(value).strip()
            )

    return render(
        request,
        "extractor/select_columns.html",
        {
            "columns": columns,
        },
    )


def export_data(request):

    selected_columns = request.POST.getlist(
        "columns"
    )

    export_format = request.POST.get(
        "format"
    )

    json_data = request.session.get(
        "extractor_data"
    )

    if not json_data:

        return redirect(
            "extractor_upload"
        )

    raw_df = pd.read_json(
        io.StringIO(json_data)
    )

    header_row = int(
        request.session.get(
            "header_row",
            1
        )
    )

    start_row = int(
        request.session.get(
            "start_row",
            2
        )
    )

    end_row = int(
        request.session.get(
            "end_row",
            len(raw_df)
        )
    )

    headers = raw_df.iloc[
        header_row - 1
    ]

    clean_headers = []

    for index, value in enumerate(headers):

        if pd.isna(value):

            clean_headers.append(
                f"Column_{index + 1}"
            )

        else:

            clean_headers.append(
                str(value).strip()
            )

    if start_row <= header_row:

        start_row = header_row + 1

    df = raw_df.iloc[
        start_row - 1:end_row
    ].copy()

    df.columns = clean_headers

    df = df.dropna(
        how="all"
    )

    if len(df) > 0:

        first_row = [

            str(x).strip()

            for x in df.iloc[0].tolist()

        ]

        if first_row == clean_headers:

            df = df.iloc[1:]

    valid_columns = [

        col

        for col in selected_columns

        if col in df.columns

    ]

    if not valid_columns:

        return HttpResponse(
            "No valid columns selected."
        )

    df = df[
        valid_columns
    ]

    if export_format == "csv":

        response = HttpResponse(
            content_type="text/csv"
        )

        response[
            "Content-Disposition"
        ] = (
            'attachment; filename="extracted.csv"'
        )

        df.to_csv(
            response,
            index=False
        )

        return response

    response = HttpResponse(
        content_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response[
        "Content-Disposition"
    ] = (
        'attachment; filename="extracted.xlsx"'
    )

    df.to_excel(
        response,
        index=False
    )

    return response