import pandas as pd

from datetime import date

from .models import Student


def import_students_from_excel(excel_file):

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
                    ""
                )
            )
        ).strip()

        if not student_name:
            continue

        # Class
        student_class = str(
            row.get(
                "student_class",
                ""
            )
        ).strip()

        # Fix numeric classes
        class_mapping = {
            "1": "Grade IA",
            "2": "Grade II",
            "3": "Grade III",
            "4": "Grade IV",
            "5": "Grade V",
            "6": "Grade VI",
            "7": "Grade VII",
            "8": "Grade VIII",
            "9": "Grade IX",
        }

        if student_class in class_mapping:
            student_class = class_mapping[
                student_class
            ]

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