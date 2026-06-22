from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import role_required

from .models import StudentEnrollment

from .forms import ExcelUploadForm
from .forms import StudentForm
from .models import Student
from .services import import_students_from_excel
from attendance.models import Attendance
from exams.models import ExamResult
from fees.models import Fee
from academics.models import AcademicYear

@role_required(
    "ADMIN",
    "TEACHER",
)
def student_profile(
    request,
    student_id,
):

    student = get_object_or_404(
        Student,
        id=student_id,
    )

    results = ExamResult.objects.filter(
        student=student
    ).order_by(
        "-created_at"
    )

    attendance_records = Attendance.objects.filter(
        student=student
    )

    fees = Fee.objects.filter(
        student=student
    )

    total_attendance = attendance_records.count()

    present_count = attendance_records.filter(
        status="Present"
    ).count()

    attendance_percentage = 0

    if total_attendance > 0:

        attendance_percentage = round(
            (
                present_count
                /
                total_attendance
            ) * 100,
            2,
        )

    pending_fee = fees.filter(
        status="Pending"
    )

    return render(
        request,
        "students/student_profile.html",
        {
            "student": student,
            "results": results,
            "attendance_records": attendance_records,
            "fees": fees,
            "attendance_percentage":
            attendance_percentage,
            "pending_fee_count":
            pending_fee.count(),
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def student_classes(
    request,
    year_id,
):

    year = get_object_or_404(
        AcademicYear,
        id=year_id,
    )

    return render(
        request,
        "students/student_classes.html",
        {
            "class_choices":
            Student.CLASS_CHOICES,

            "year": year,
        },
    )

@role_required(
    "ADMIN",
    "TEACHER",
)
def student_list(request):

    students = Student.objects.all()

    enrollments = StudentEnrollment.objects.filter(
    academic_year_id=year_id,
    student_class=class_name,
).select_related(
    "student"
)

    search_query = request.GET.get(
        "search",
        "",
    ).strip()

    if search_query:

        students = students.filter(

        Q(
            name__icontains=search_query
        )
        |
        Q(
            student_id__icontains=search_query
        )

    )

    class_filter = request.GET.get(
        "class",
        "",
    ).strip()

    if class_filter:

        students = students.filter(
            student_class=class_filter
        )

    paginator = Paginator(
        students,
        10,
    )

    page_number = request.GET.get(
        "page"
    )

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "students/student_list.html",
        {
            "page_obj": page_obj,
            "search_query": search_query,
            "class_filter": class_filter,
            "class_choices": Student.CLASS_CHOICES,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def add_student(request):

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "student_list"
            )
        print(form.errors)

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
        },
    )


@role_required("ADMIN")
def edit_student(
    request,
    id,
):

    student = get_object_or_404(
        Student,
        id=id,
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "student_list"
            )

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
            "student": student,
        },
    )


@role_required("ADMIN")
def delete_student(
    request,
    id,
):

    student = get_object_or_404(
        Student,
        id=id,
    )

    if request.method == "POST":

        student.delete()

        return redirect(
            "student_list"
        )

    return render(
        request,
        "students/delete_student.html",
        {
            "student": student,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def import_students(request):

    if request.method == "POST":

        form = ExcelUploadForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            import_students_from_excel(
                request.FILES[
                    "excel_file",
                ]
            )

            return redirect(
                "student_list"
            )

    else:

        form = ExcelUploadForm()

    return render(
        request,
        "students/import_students.html",
        {
            "form": form,
        },
    )
@role_required(
    "ADMIN",
    "TEACHER",
)
def student_dashboard(
    request,
    year_id,
    class_name,
):

    year = get_object_or_404(
        AcademicYear,
        id=year_id,
    )

    return render(
        request,
        "students/student_dashboard.html",
        {
            "class_name": class_name,
            "year": year,
        },
    )
@role_required(
    "ADMIN",
    "TEACHER",
)

def class_student_list(
    request,
    year_id,
    class_name,
):

    enrollments = StudentEnrollment.objects.filter(
        academic_year_id=year_id,
        student_class=class_name,
    ).select_related(
        "student"
    ).order_by(
        "student__name"
    )

    year = get_object_or_404(
        AcademicYear,
        id=year_id,
    )

    return render(
        request,
        "students/class_student_list.html",
        {
            "enrollments": enrollments,
            "class_name": class_name,
            "year": year,
        },
    )
    
@role_required(
    "ADMIN",
    "TEACHER",
)
def import_class_students(
    request,
    year_id,
    class_name,
):

    year = get_object_or_404(
        AcademicYear,
        id=year_id,
    )

    if request.method == "POST":

        form = ExcelUploadForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            import_students_from_excel(
                request.FILES["excel_file"],
                selected_class=class_name,
                academic_year=year,
            )

            return redirect(
                "class_student_list",
                year_id=year.id,
                class_name=class_name,
            )

    else:

        form = ExcelUploadForm()

    return render(
        request,
        "students/import_students.html",
        {
            "form": form,
            "class_name": class_name,
            "year": year,
        },
    )
def student_years(request):

    years = AcademicYear.objects.all()

    return render(
        request,
        "students/student_years.html",
        {
            "years": years,
        },
    )