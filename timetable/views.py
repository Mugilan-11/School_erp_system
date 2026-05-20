from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Timetable
from .forms import TimetableForm

import pandas as pd

from .forms import (
    TimetableForm,
    TimetableExcelUploadForm
)

@login_required
def import_timetable(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER'
    ]:
        return redirect('login')

    if request.method == 'POST':

        form = TimetableExcelUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            excel_file = request.FILES['excel_file']

            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():

                Timetable.objects.create(

                    class_name=row['class_name'],

                    subject=row['subject'],

                    teacher=row['teacher'],

                    day=row['day'],

                    start_time=row['start_time'],

                    end_time=row['end_time']

                )

            return redirect('timetable_list')

    else:

        form = TimetableExcelUploadForm()

    context = {

        'form': form

    }

    return render(
        request,
        'timetable/import_timetable.html',
        context
    )


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