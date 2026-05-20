from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Teacher
from .forms import TeacherForm


@login_required
def teacher_list(request):

    if request.user.role != 'ADMIN':
        return redirect('login')

    teachers = Teacher.objects.all()

    context = {

        'teachers': teachers

    }

    return render(
        request,
        'teachers/teacher_list.html',
        context
    )


@login_required
def add_teacher(request):

    if request.user.role != 'ADMIN':
        return redirect('login')

    if request.method == 'POST':

        form = TeacherForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('teacher_list')

    else:

        form = TeacherForm()

    context = {

        'form': form

    }

    return render(
        request,
        'teachers/add_teacher.html',
        context
    )