from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
import pandas as pd

from .forms import ExcelUploadForm


@login_required
def student_list(request):

    if request.user.role not in ['ADMIN', 'TEACHER']:
        return redirect('login')

    students = Student.objects.all()

    search_query = request.GET.get('search')

    class_filter = request.GET.get('class')

    if search_query:

        students = students.filter(
            first_name__icontains=search_query
        ) | students.filter(
            last_name__icontains=search_query
        ) | students.filter(
            admission_no__icontains=search_query
        )

    if class_filter:

        students = students.filter(
            student_class=class_filter
        )

    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(
        request,
        'students/student_list.html',
        context
    )


@login_required
def add_student(request):

    if request.user.role not in ['ADMIN', 'TEACHER']:
        return redirect('login')

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm()

    context = {
        'form': form
    }

    return render(
        request,
        'students/add_student.html',
        context
    )


@login_required
def edit_student(request, id):

    if request.user.role != 'ADMIN':
        return redirect('login')

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    context = {
        'form': form
    }

    return render(
        request,
        'students/edit_student.html',
        context
    )


@login_required
def delete_student(request, id):

    if request.user.role != 'ADMIN':
        return redirect('login')

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('student_list')

@login_required
def import_students(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER'
    ]:
        return redirect('login')

    if request.method == 'POST':

        form = ExcelUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            excel_file = request.FILES['excel_file']

            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():

                Student.objects.create(

                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    admission_no=row['admission_no'],
                    student_class=str(row['student_class']),
                    gender=row['gender'],
                    date_of_birth=row['date_of_birth'],
                    address=row['address']

                )

            return redirect('student_list')

    else:

        form = ExcelUploadForm()

    context = {

        'form': form

    }

    return render(
        request,
        'students/import_students.html',
        context
    )