from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

import json


def index(request):
    return render(request, 'core/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(["GET"])
def get_level(request):
    level_number = int(request.GET.get('lvl', 1))
    arr = []
    if level_number == 1:
        arr = (
            (1, 1, 1),
            (1, 0, 1),
            (1, 1, 1)
        )
    elif level_number == 2:
        arr = (
            (1, 1, 1, 1, 1),
            (1, 0, 1, 0, 1),
            (1, 0, 0, 0, 1),
            (1, 0, 1, 0, 1),
            (1, 1, 1, 1, 1)
        )
    elif level_number == 3:
        arr = (
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        )
    elif level_number == 4:
        arr = (
            (1, 1, 1, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 0, 0, 1),
            (1, 1, 1, 1),
        )
    return HttpResponse(json.dumps(arr))

@require_http_methods(["GET"])
def get_path(request):
    arr = ((1, 2), (2, 2), (3, 4))
    return HttpResponse(json.dumps(arr))
