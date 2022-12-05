from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from core.libs.level_wrapper.level_wrapper import LevelWrapper
from core.libs.game_engine.game_engine import GameEngine


def index(request):
    return render(request, 'core/index.html')

@require_http_methods(["GET"])
def get_level(request):
    level_number = int(request.GET.get('lvl', 1))

    lvl = LevelWrapper(level_number)
    print(lvl.get_x_start())
    return JsonResponse({
        'grid': lvl.get_level(),
        'x_start': lvl.get_x_start(),
        'y_start': lvl.get_y_start(),
        'x_finish': lvl.get_x_finish(),
        'y_finish': lvl.get_y_finish(),
        'number': lvl.get_num(),
    })

@require_http_methods(["GET"])
def get_path(request):
    level_number = int(request.GET.get('lvl', 1))
    unparsed_code = request.GET.get('code', '')

    try:
        game_engine = GameEngine(level_number, unparsed_code)
        result = game_engine.execute()
        return JsonResponse({
            'is_win': result.win,
            'path': result.way,
            'syntax_error': False,
        })
    except:
        return JsonResponse({
            'syntax_error': True
        })
