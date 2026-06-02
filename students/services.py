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

        admission_no = str(
            row.get("admission_no", "")
        ).strip()

        if not admission_no:
            continue

        defaults = {
            "first_name": str(
                row.get("first_name", "")
            ).strip(),

            "last_name": str(
                row.get("last_name", "")
            ).strip(),

            # Default Grade IA
            "student_class": str(
                row.get("student_class", "3")
            ).strip(),

            "gender": str(
                row.get("gender", "Male")
            ).strip(),

            # Default DOB
            "date_of_birth": row.get(
                "date_of_birth",
                date(2018, 1, 1)
            ),

            # Default address
            "address": str(
                row.get("address", "Not Available")
            ).strip(),
        }

        student, created = Student.objects.update_or_create(
            admission_no=admission_no,
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