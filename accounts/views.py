from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from students.models import Student
from accounts.models import CustomUser


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'ADMIN':
                return redirect('admin_dashboard')

            elif user.role == 'TEACHER':
                return redirect('teacher_dashboard')

            elif user.role == 'STUDENT':
                return redirect('student_dashboard')

            elif user.role == 'PARENT':
                return redirect('parent_dashboard')

        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def admin_dashboard(request):

    if request.user.role != 'ADMIN':
        return redirect('login')

    from students.models import Student
    from accounts.models import CustomUser

    total_students = Student.objects.count()

    total_teachers = CustomUser.objects.filter(
        role='TEACHER'
    ).count()

    total_admins = CustomUser.objects.filter(
        role='ADMIN'
    ).count()

    recent_students = Student.objects.order_by(
        '-id'
    )[:5]

    context = {

        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_admins': total_admins,
        'recent_students': recent_students,
    }

    return render(
        request,
        'accounts/admin_dashboard.html',
        context
    )

@login_required
def teacher_dashboard(request):

    if request.user.role != 'TEACHER':
        return redirect('login')

    from students.models import Student

    total_students = Student.objects.count()

    context = {

        'total_students': total_students,

    }

    return render(
        request,
        'accounts/teacher_dashboard.html',
        context
    )


@login_required
def student_dashboard(request):

    if request.user.role != 'STUDENT':
        return redirect('login')

    return render(
        request,
        'accounts/student_dashboard.html'
    )


@login_required
def parent_dashboard(request):

    if request.user.role != 'PARENT':
        return redirect('login')

    return render(
        request,
        'accounts/parent_dashboard.html'
    )