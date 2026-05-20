from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import ExamResult, SubjectMark
from .forms import ExamResultForm


@login_required
def result_list(request):

    if request.user.role not in ['ADMIN', 'TEACHER']:
        return redirect('login')

    results = ExamResult.objects.all().order_by(
        '-created_at'
    )

    context = {
        'results': results
    }

    return render(
        request,
        'exams/result_list.html',
        context
    )


@login_required
def add_result(request):

    if request.user.role not in ['ADMIN', 'TEACHER']:
        return redirect('login')

    if request.method == 'POST':

        form = ExamResultForm(request.POST)

        if form.is_valid():

            exam_result = form.save()

            subject_names = request.POST.getlist(
                'subject_name'
            )

            marks_obtained = request.POST.getlist(
                'mark_obtained'
            )

            maximum_marks = request.POST.getlist(
                'maximum_mark'
            )

            for i in range(len(subject_names)):

                SubjectMark.objects.create(

                    exam_result=exam_result,

                    subject_name=subject_names[i],

                    mark_obtained=marks_obtained[i],

                    maximum_mark=maximum_marks[i],
                )

            exam_result.calculate_result()

            return redirect('result_list')

    else:

        form = ExamResultForm()

    context = {
        'form': form
    }

    return render(
        request,
        'exams/add_result.html',
        context
    )


@login_required
def report_card(request, id):

    if request.user.role not in ['ADMIN', 'TEACHER']:
        return redirect('login')

    result = get_object_or_404(
        ExamResult,
        id=id
    )

    subjects = SubjectMark.objects.filter(
        exam_result=result
    )

    context = {

        'result': result,
        'subjects': subjects,
    }

    return render(
        request,
        'exams/report_card.html',
        context
    )