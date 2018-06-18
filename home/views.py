from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def delivery_info(request):
    return render(request, "delivery_info.html")


def club_herculean(request):
    return render(request, "club_herculean.html")