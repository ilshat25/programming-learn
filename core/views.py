from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'core/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")