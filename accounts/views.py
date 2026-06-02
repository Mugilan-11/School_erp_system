from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .decorators import role_required

ROLE_REDIRECTS = {
    "ADMIN": "admin_dashboard",
    "TEACHER": "teacher_dashboard",
    "STUDENT": "student_dashboard",
    "PARENT": "parent_dashboard",
}


def role_login(request, role, template_name):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user and user.role == role:
            login(request, user)
            return redirect(ROLE_REDIRECTS[role])

        return render(
            request,
            template_name,
            {
                "error": "Invalid credentials for selected role",
            },
        )

    return render(request, template_name)


def admin_login(request):
    return role_login(
        request,
        "ADMIN",
        "accounts/admin_login.html",
    )


def teacher_login(request):
    return role_login(
        request,
        "TEACHER",
        "accounts/teacher_login.html",
    )


def student_login(request):
    return role_login(
        request,
        "STUDENT",
        "accounts/student_login.html",
    )


def parent_login(request):
    return role_login(
        request,
        "PARENT",
        "accounts/parent_login.html",
    )


def logout_view(request):
    logout(request)
    return redirect("/")


@role_required("ADMIN")
def admin_dashboard(request):
    from exams.models import ExamResult
    from students.models import Student
    from teachers.models import Teacher
    from timetable.models import Timetable

    context = {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_results": ExamResult.objects.count(),
        "total_timetables": Timetable.objects.count(),
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context,
    )


@role_required("TEACHER")
def teacher_dashboard(request):
    return render(
        request,
        "accounts/teacher_dashboard.html",
    )


@role_required("STUDENT")
def student_dashboard(request):
    return render(
        request,
        "accounts/student_dashboard.html",
    )


@role_required("PARENT")
def parent_dashboard(request):
    return render(
        request,
        "accounts/parent_dashboard.html",
    )