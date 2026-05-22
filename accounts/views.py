from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


# =====================================
# LOGIN HELPERS
# =====================================

def role_login(request, role, template_name):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None and user.role == role:

            login(request, user)

            if role == 'ADMIN':

                return redirect('admin_dashboard')

            elif role == 'TEACHER':

                return redirect('teacher_dashboard')

            elif role == 'STUDENT':

                return redirect('student_dashboard')

            elif role == 'PARENT':

                return redirect('parent_dashboard')

        return render(

            request,

            template_name,

            {

                'error':

                'Invalid credentials for selected role'

            }

        )

    return render(request, template_name)


# =====================================
# ROLE LOGINS
# =====================================

def admin_login(request):

    return role_login(

        request,

        'ADMIN',

        'accounts/admin_login.html'

    )


def teacher_login(request):

    return role_login(

        request,

        'TEACHER',

        'accounts/teacher_login.html'

    )


def student_login(request):

    return role_login(

        request,

        'STUDENT',

        'accounts/student_login.html'

    )


def parent_login(request):

    return role_login(

        request,

        'PARENT',

        'accounts/parent_login.html'

    )


# =====================================
# LOGOUT
# =====================================

def logout_view(request):

    logout(request)

    return redirect('/')


# =====================================
# ADMIN DASHBOARD
# =====================================

@login_required
def admin_dashboard(request):

    if request.user.role != 'ADMIN':

        return redirect('login')

    from students.models import Student
    from teachers.models import Teacher
    from exams.models import ExamResult
    from timetable.models import Timetable

    context = {

        'total_students': Student.objects.count(),

        'total_teachers': Teacher.objects.count(),

        'total_results': ExamResult.objects.count(),

        'total_timetables': Timetable.objects.count(),

    }

    return render(

        request,

        'accounts/admin_dashboard.html',

        context

    )


# =====================================
# TEACHER DASHBOARD
# =====================================

@login_required
def teacher_dashboard(request):

    if request.user.role != 'TEACHER':

        return redirect('login')

    return render(

        request,

        'accounts/teacher_dashboard.html'

    )


# =====================================
# STUDENT DASHBOARD
# =====================================

@login_required
def student_dashboard(request):

    if request.user.role != 'STUDENT':

        return redirect('login')

    return render(

        request,

        'accounts/student_dashboard.html'

    )


# =====================================
# PARENT DASHBOARD
# =====================================

@login_required
def parent_dashboard(request):

    if request.user.role != 'PARENT':

        return redirect('login')

    return render(

        request,

        'accounts/parent_dashboard.html'

    )