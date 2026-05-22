from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    login,
    logout
)


# =====================================
# ADMIN LOGIN
# =====================================

def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None and user.role == 'ADMIN':

            login(request, user)

            return redirect(
                'admin_dashboard'
            )

        return render(

            request,

            'accounts/admin_login.html',

            {

                'error':

                'Only admins can login here'

            }

        )

    return render(
        request,
        'accounts/admin_login.html'
    )


# =====================================
# TEACHER LOGIN
# =====================================

def teacher_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None and user.role == 'TEACHER':

            login(request, user)

            return redirect(
                'teacher_dashboard'
            )

        return render(

            request,

            'accounts/teacher_login.html',

            {

                'error':

                'Only teachers can login here'

            }

        )

    return render(
        request,
        'accounts/teacher_login.html'
    )


# =====================================
# STUDENT LOGIN
# =====================================

def student_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None and user.role == 'STUDENT':

            login(request, user)

            return redirect(
                'student_dashboard'
            )

        return render(

            request,

            'accounts/student_login.html',

            {

                'error':

                'Only students can login here'

            }

        )

    return render(
        request,
        'accounts/student_login.html'
    )


# =====================================
# PARENT LOGIN
# =====================================

def parent_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None and user.role == 'PARENT':

            login(request, user)

            return redirect(
                'parent_dashboard'
            )

        return render(

            request,

            'accounts/parent_login.html',

            {

                'error':

                'Only parents can login here'

            }

        )

    return render(
        request,
        'accounts/parent_login.html'
    )


# =====================================
# LOGOUT
# =====================================

def logout_view(request):

    logout(request)

    return redirect('home')


# =====================================
# DASHBOARDS
# =====================================

def admin_dashboard(request):

    return render(
        request,
        'accounts/admin_dashboard.html'
    )


def teacher_dashboard(request):

    return render(
        request,
        'accounts/teacher_dashboard.html'
    )


def student_dashboard(request):

    return render(
        request,
        'accounts/student_dashboard.html'
    )


def parent_dashboard(request):

    return render(
        request,
        'accounts/parent_dashboard.html'
    )