from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Timetable
from .forms import TimetableForm


@login_required
def timetable_list(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER',
        'STUDENT'

    ]:
        return redirect('login')

    classes = Timetable.objects.values(
        'class_name',
        'section'
    ).distinct()

    context = {
        'classes': classes
    }

    return render(
        request,
        'timetable/timetable_list.html',
        context
    )


@login_required
def class_timetable(
    request,
    class_name,
    section
):

    timetable_entries = Timetable.objects.filter(
        class_name=class_name,
        section=section
    ).order_by(
        'day',
        'start_time'
    )

    context = {

        'timetable_entries': timetable_entries,
        'class_name': class_name,
        'section': section,
    }

    return render(
        request,
        'timetable/class_timetable.html',
        context
    )


@login_required
def add_timetable(request):

    if request.user.role != 'ADMIN':
        return redirect('login')

    if request.method == 'POST':

        form = TimetableForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('timetable_list')

    else:

        form = TimetableForm()

    context = {
        'form': form
    }

    return render(
        request,
        'timetable/add_timetable.html',
        context
    )