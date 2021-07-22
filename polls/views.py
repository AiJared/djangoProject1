from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World. You'r at the polls index.")