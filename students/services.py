import pandas as pd

from datetime import date

from .models import Student


def import_students_from_excel(excel_file,selected_class=None):

    if excel_file.name.endswith(".csv"):
        df = pd.read_csv(excel_file)
    else:
        df = pd.read_excel(excel_file)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    created_count = 0
    updated_count = 0

    for _, row in df.iterrows():

        # Student ID
        student_id = str(
            row.get(
                "student_id",
                row.get(
                    "admission_no",
                    ""
                )
            )
        ).strip()

        if not student_id:
            continue

        # Student Name
        student_name = str(
    row.get(
        "student_name",
        row.get(
            "name",
            row.get(
                "names",
                ""
            )
        )
    )
).strip()

        if not student_name:
            continue

        # Class
        student_class = selected_class

        defaults = {
    "name": student_name,

    "student_class": (
        student_class
        if student_class
        else None
    ),

    "gender": (
        str(row.get("gender")).strip()
        if row.get("gender")
        else None
    ),

    "date_of_birth": row.get(
        "date_of_birth",
        None
    ),

    "address": (
        str(row.get("address")).strip()
        if row.get("address")
        else None
    ),

    "first_name": student_name,

    "last_name": "",

    "admission_no": student_id,

    "student_id": student_id,
}
        student, created = Student.objects.update_or_create(
            student_id=student_id,
            defaults=defaults,
        )

        if created:
            created_count += 1
        else:
            updated_count += 1

    return {
        "created": created_count,
        "updated": updated_count,
    }