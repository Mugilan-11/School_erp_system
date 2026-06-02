from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import role_required

from .forms import ExcelUploadForm
from .forms import StudentForm
from .models import Student
from .services import import_students_from_excel


@role_required(
    "ADMIN",
    "TEACHER",
)
def student_classes(request):

    return render(
        request,
        "students/student_classes.html",
        {
            "class_choices":
            Student.CLASS_CHOICES
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def student_list(request):

    students = Student.objects.all()

    search_query = request.GET.get(
        "search",
        "",
    ).strip()

    if search_query:

        students = students.filter(

            Q(
                first_name__icontains=search_query
            )
            |
            Q(
                last_name__icontains=search_query
            )
            |
            Q(
                admission_no__icontains=search_query
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
                    "excel_file"
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