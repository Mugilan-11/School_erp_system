from django.shortcuts import render


def home(request):

    return render(
        request,
        'website/home.html'
    )


def about(request):

    return render(
        request,
        'website/about.html'
    )


def academics(request):

    return render(
        request,
        'website/academics.html'
    )


def admissions(request):

    return render(
        request,
        'website/admissions.html'
    )


def facilities(request):

    return render(
        request,
        'website/facilities.html'
    )


def gallery(request):

    return render(
        request,
        'website/gallery.html'
    )


def contact(request):

    return render(
        request,
        'website/contact.html'
    )


def login_options(request):

    return render(
        request,
        'website/login_options.html'
    )