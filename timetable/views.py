from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import pandas as pd

from .models import Timetable

from .forms import (
    TimetableForm,
    TimetableExcelUploadForm
)

from accounts.models import CustomUser


@login_required
def timetable_list(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'

    ]:
        return redirect('login')

    timetables = Timetable.objects.all()

    class_filter = request.GET.get('class')

    if class_filter:

        timetables = timetables.filter(
            student_class=class_filter
        )

    context = {

        'timetables': timetables

    }

    return render(
        request,
        'timetable/timetable_list.html',
        context
    )


@login_required
def add_timetable(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER'

    ]:
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

                teacher = CustomUser.objects.filter(

                    username=row['teacher']

                ).first()

                if teacher:

                    Timetable.objects.create(

                        student_class=row['student_class'],

                        subject=row['subject'],

                        teacher=teacher,

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