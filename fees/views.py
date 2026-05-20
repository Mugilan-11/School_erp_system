from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Fee
from .forms import FeeForm


@login_required
def fee_list(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'
    ]:
        return redirect('login')

    fees = Fee.objects.all()

    context = {

        'fees': fees

    }

    return render(
        request,
        'fees/fee_list.html',
        context
    )


@login_required
def add_fee(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER'
    ]:
        return redirect('login')

    if request.method == 'POST':

        form = FeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('fee_list')

    else:

        form = FeeForm()

    context = {

        'form': form

    }

    return render(
        request,
        'fees/add_fee.html',
        context
    )