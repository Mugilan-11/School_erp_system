from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import role_required

from .forms import TeacherForm
from .models import Teacher


@role_required("ADMIN")
def teacher_list(request):

    teachers = Teacher.objects.all()

    search_query = request.GET.get(
        "search",
        "",
    ).strip()

    if search_query:

        teachers = teachers.filter(
            Q(first_name__icontains=search_query)
            |
            Q(last_name__icontains=search_query)
            |
            Q(employee_id__icontains=search_query)
            |
            Q(subject__icontains=search_query)
        )

    paginator = Paginator(
        teachers,
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
        "teachers/teacher_list.html",
        {
            "page_obj": page_obj,
            "search_query": search_query,
        },
    )


@role_required("ADMIN")
def add_teacher(request):

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "teacher_list"
            )

        print("FORM ERRORS:")
        print(form.errors)

    else:

        form = TeacherForm()

    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form,
        },
    )

@role_required("ADMIN")
def edit_teacher(
    request,
    id,
):

    teacher = get_object_or_404(
        Teacher,
        id=id,
    )

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES,
            instance=teacher,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "teacher_list"
            )

    else:

        form = TeacherForm(
            instance=teacher
        )

    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form,
            "teacher": teacher,
        },
    )


@role_required("ADMIN")
def delete_teacher(
    request,
    id,
):

    teacher = get_object_or_404(
        Teacher,
        id=id,
    )

    if request.method == "POST":

        teacher.delete()

        return redirect(
            "teacher_list"
        )

    return render(
        request,
        "teachers/delete_teacher.html",
        {
            "teacher": teacher,
        },
    )
