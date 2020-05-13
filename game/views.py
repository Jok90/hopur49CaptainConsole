from django.shortcuts import render, get_object_or_404
from game.models import Game



# Create your views here.
def index(request):
    return render(request, 'game/index.html', context={'games': Game.objects.all().order_by('name')})

def get_game_by_id(request,id):
    return render(request, 'game/game_details.html',{
        'game': get_object_or_404(Game, pk=id)
    })