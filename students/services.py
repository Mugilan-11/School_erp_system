import pandas as pd

from .models import Student


def import_students_from_excel(excel_file):

    df = pd.read_excel(excel_file)

    students = []

    existing_admission_numbers = set(
        Student.objects.values_list(
            "admission_no",
            flat=True,
        )
    )

    for _, row in df.iterrows():

        admission_no = str(
            row["admission_no"]
        ).strip()

        if admission_no in existing_admission_numbers:
            continue

        students.append(
            Student(
                first_name=str(
                    row["first_name"]
                ).strip(),

                last_name=str(
                    row["last_name"]
                ).strip(),

                admission_no=admission_no,

                student_class=str(
                    row["student_class"]
                ).strip(),

                gender=str(
                    row["gender"]
                ).strip(),

                date_of_birth=row[
                    "date_of_birth"
                ],

                address=str(
                    row["address"]
                ).strip(),
            )
        )

    Student.objects.bulk_create(students)

    return len(students)